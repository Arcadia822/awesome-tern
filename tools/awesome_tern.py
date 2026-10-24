# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6"]
# ///
"""Maintain awesome-tern. list.yml is the source; README.md is generated from it.

Commands:
  check      validate list.yml
  build      regenerate README.md
  refresh    fetch stars and status for GitHub entries into metadata.json
  discover   print recently created Tern repositories that aren't listed
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import posixpath
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Iterator
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIST = ROOT / "list.yml"
METADATA = ROOT / "metadata.json"
README = ROOT / "README.md"
KIND_DIR = ROOT / "assets" / "kinds"

GITHUB_REPO_URL = re.compile(r"^https://github\.com/([\w.-]+)/([\w.-]+)/?$")
INACTIVE_AFTER = dt.timedelta(days=180)
SORTS = {"stars", "manual"}
# kind: (legend text, light-theme colour, dark-theme colour). Each kind renders as a pill image.
KINDS = {
    "plugin": ("Luau plugin", "#0969da", "#4493f8"),
    "app": ("App drawn natively over TSP", "#8250df", "#ab7df8"),
    "extension": ("Runs inside your coding agent", "#1a7f37", "#3fb950"),
    "companion": ("Runs outside Tern", "#bc4c00", "#db6d28"),
    "library": ("SDK or protocol library", "#bf3989", "#db61a2"),
    "config": ("Nix package or dotfiles", "#9a6700", "#d29922"),
    "docs": ("Documentation", "#59636e", "#9198a1"),
}
# Repository links, optionally into a folder whose README describes the entry.
GITHUB_TREE_URL = re.compile(r"^https://github\.com/([\w.-]+)/([\w.-]+)(?:/tree/[^/]+/(.+?))?/?$")
README_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)|<img[^>]*\bsrc=[\"']([^\"']+)", re.I)
NOT_SCREENSHOT = re.compile(
    r"shields\.io|badge|badgen|codecov|deepwiki|/actions/workflows/|star-history|contrib\.rocks|buymeacoffee|ko-fi"
    r"|(?<![a-z])(?:logo|icon|banner|hero)(?![a-z])",
    re.I,
)
SCREENSHOT_TYPES = (".png", ".jpg", ".jpeg", ".gif", ".webp")


# --------------------------------------------------------------------------- data


def load_list() -> dict:
    try:
        with LIST.open(encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as err:
        raise SystemExit(f"error: list.yml is not valid YAML\n{err}") from None


def load_metadata() -> dict:
    return json.loads(METADATA.read_text()) if METADATA.exists() else {}


def walk(sections: list[dict], depth: int = 0) -> Iterator[tuple[dict, int]]:
    for s in sections:
        yield s, depth
        yield from walk(s.get("sections", []), depth + 1)


def all_entries(data: dict) -> Iterator[dict]:
    for s, _ in walk(data["sections"]):
        yield from s.get("entries", [])


def entry_repo(entry: dict) -> str | None:
    """owner/name for GitHub metadata: explicit `repo`, else a repository URL."""
    if entry.get("repo"):
        return entry["repo"]
    m = GITHUB_REPO_URL.match(entry["url"])
    return f"{m[1]}/{m[2]}" if m else None


# ----------------------------------------------------------------------- validate


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    for key in ("title", "tagline", "sections"):
        if not data.get(key):
            errors.append(f"list.yml: missing {key}")
    seen: dict[str, str] = {}
    anchors = {"contents", "legend", "contributing"}
    for s, _ in walk(data.get("sections", [])):
        title = s.get("title") or "?"
        if not s.get("title"):
            errors.append("a section is missing its title")
        elif anchor(title) in anchors:
            errors.append(f"{title}: another heading already uses this title")
        anchors.add(anchor(title))
        if s.get("sort", "stars") not in SORTS:
            errors.append(f"{title}: sort must be one of {sorted(SORTS)}")
        for e in s.get("entries", []):
            where = f"{title} > {e.get('name') or e.get('url') or '?'}"
            for field in ("name", "url", "kind", "description"):
                if not e.get(field):
                    errors.append(f"{where}: missing {field}")
            unknown = set(e) - {"name", "url", "kind", "description", "repo", "screenshot"}
            if unknown:
                errors.append(f"{where}: unknown fields {sorted(unknown)}")
            if e.get("kind") and e["kind"] not in KINDS:
                errors.append(f"{where}: kind must be one of {list(KINDS)}")
            shot = e.get("screenshot")
            if shot is not None and shot != "none" and not str(shot).startswith("https://"):
                errors.append(f"{where}: screenshot must be an https:// URL or none")
            url = e.get("url", "")
            if url and not url.startswith("https://"):
                errors.append(f"{where}: url must start with https://")
            if url in seen:
                errors.append(f"{where}: also listed under {seen[url]}")
            seen[url] = title
            desc = (e.get("description") or "").strip()
            if desc:
                if desc[0].islower():
                    errors.append(f"{where}: description must not start with a lowercase letter")
                if not desc.endswith("."):
                    errors.append(f"{where}: description must end with a period")
                if "\n" in desc:
                    errors.append(f"{where}: description must be one line")
    return errors


def cmd_check(_args) -> int:
    errors = validate(load_list())
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    return 1 if errors else 0


# -------------------------------------------------------------------------- build


def anchor(title: str) -> str:
    return re.sub(r"[^\w\- ]", "", title.strip().lower()).replace(" ", "-")


def age(pushed: str, today: dt.date) -> str:
    """Time since the last push, in units coarse enough that it rarely changes overnight."""
    days = (today - dt.date.fromisoformat(pushed)).days
    if days < 1:
        return "today"
    if days < 14:
        return f"{days}d"
    if days < 60:
        return f"{days // 7}w"
    if days < 365:
        return f"{days // 30}mo"
    return f"{days // 365}y"


def compact(stars: int) -> str:
    return f"{stars / 1000:.1f}k" if stars >= 1000 else str(stars)


def chips(entry: dict, meta: dict, today: dt.date) -> list[str]:
    """Stars, time since the last push and status from the last refresh, for GitHub-backed entries.

    Each chip is one code span with non-breaking spaces, so a narrow column stacks whole chips
    instead of splitting one.
    """
    repo = entry_repo(entry)
    info = meta.get(repo) if repo else None
    if not info:
        return []
    if info.get("status") == "unavailable":
        return ["`unavailable`"]
    out = [f"`★\u00a0{compact(info['stars'])}`", f"`{age(info['pushed'], today)}`"]
    if info.get("status"):
        out.append(f"`{info['status']}`")
    return out


def entry_readme(entry: dict) -> tuple[str, str] | None:
    """(owner/name, folder) of the README that describes an entry, if it links to a repository or folder."""
    m = GITHUB_TREE_URL.match(entry["url"])
    if not m:
        return None
    return entry.get("repo") or f"{m[1]}/{m[2]}", m[3] or ""


def screenshot(entry: dict, meta: dict) -> str | None:
    if entry.get("screenshot"):
        return None if entry["screenshot"] == "none" else entry["screenshot"]
    where = entry_readme(entry)
    if not where:
        return None
    return (meta.get(where[0]) or {}).get("screenshots", {}).get(where[1])


def ordered(section: dict, meta: dict) -> list[dict]:
    entries = section.get("entries", [])
    if section.get("sort", "stars") == "manual":
        return entries

    def stars(e):
        repo = entry_repo(e)
        return (meta.get(repo) or {}).get("stars", -1) if repo else -1

    return sorted(entries, key=lambda e: (-stars(e), e["name"].lower()))


def pill(kind: str) -> str:
    src = f"{KIND_DIR.relative_to(ROOT).as_posix()}/{kind}.svg"
    return f'<a href="#legend"><img src="{src}" alt="{kind}" align="absmiddle"></a>'


def pill_svg(kind: str, light: str, dark: str) -> str:
    """A pill styled like a GitHub issue label, recoloured for dark themes."""
    width = round(len(kind) * 6.7 + 16)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" viewBox="0 0 {width} 20" role="img" aria-label="{kind}">\n'
        f"<title>{kind}</title>\n"
        f"<style>.b{{fill:{light};fill-opacity:.12;stroke:{light};stroke-opacity:.4}}"
        f'.t{{fill:{light};font:500 12px -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif}}'
        f"@media (prefers-color-scheme:dark){{.b{{fill:{dark};stroke:{dark}}}.t{{fill:{dark}}}}}</style>\n"
        f'<rect class="b" x=".5" y=".5" width="{width - 1}" height="19" rx="9.5"/>\n'
        f'<text class="t" x="{width / 2:g}" y="14" text-anchor="middle">{kind}</text>\n'
        "</svg>\n"
    )


def count(section: dict) -> int:
    return len(section.get("entries", [])) + sum(count(s) for s in section.get("sections", []))


def cell(text: str) -> str:
    return text.strip().replace("|", "\\|")


def entry_row(e: dict, meta: dict, today: dt.date) -> str:
    left = f"**[{cell(e['name'])}]({e['url']})**<br>{pill(e['kind'])}"
    if c := chips(e, meta, today):
        left += "<br>" + " ".join(c)
    right = cell(e["description"])
    if shot := screenshot(e, meta):
        right += f'<details><summary>Screenshot</summary><img src="{shot}" width="520" alt="{cell(e["name"])} screenshot"></details>'
    return f"| {left} | {right} |"


def render(data: dict, meta: dict, today: dt.date) -> str:
    out = [
        "<!-- Generated from list.yml by tools/awesome_tern.py. Edit list.yml, not this file. -->",
        "",
        f"# {data['title']}",
        "",
        f"> {data['tagline'].strip()}",
        "",
    ]
    if data.get("intro"):
        out += [data["intro"].strip(), ""]
    out += [
        "Each entry shows what kind of project it is, its GitHub stars and how long ago it was last updated; the [legend](#legend) explains the labels.",
        "",
        "## Contents",
        "",
    ]
    for s in data["sections"]:
        line = f"- **[{s['title']}](#{anchor(s['title'])})** {count(s)}"
        subs = s.get("sections", [])
        if subs:
            line += " — " + " · ".join(f"[{c['title']}](#{anchor(c['title'])})" for c in subs)
        out.append(line)
    out.append("")
    for s, depth in walk(data["sections"]):
        out += [f"{'#' * (depth + 2)} {s['title']}", ""]
        if s.get("blurb"):
            blurb = s["blurb"].strip()
            out += [blurb if "\n" in blurb else f"*{blurb}*", ""]
        items = ordered(s, meta)
        if items:
            out += ["| Project | About |", "|---|---|", *(entry_row(e, meta, today) for e in items), ""]
    out += [
        "## Legend",
        "",
        "| Label | Meaning |",
        "|---|---|",
        *(f"| {pill(k)} | {label} |" for k, (label, _, _) in KINDS.items()),
        "| `★\u00a036.4k` `3d` | GitHub stars and time since the last push |",
        "| `inactive` `archived` `unavailable` | No push in six months, archived, or the repository is gone |",
        "",
    ]
    if data.get("contributing"):
        out += ["## Contributing", "", data["contributing"].strip(), ""]
    return "\n".join(out)


def cmd_build(_args) -> int:
    data = load_list()
    errors = validate(data)
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1
    KIND_DIR.mkdir(parents=True, exist_ok=True)
    for kind, (_, light, dark) in KINDS.items():
        (KIND_DIR / f"{kind}.svg").write_text(pill_svg(kind, light, dark), encoding="utf-8")
    README.write_text(render(data, load_metadata(), dt.datetime.now(dt.UTC).date()), encoding="utf-8")
    print("wrote README.md")
    return 0


# ------------------------------------------------------------------------- github


def github_token() -> str | None:
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def github(path: str, token: str | None, accept: str = "application/vnd.github+json"):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", accept)
    req.add_header("User-Agent", "awesome-tern")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
            break
        except urllib.error.HTTPError as err:
            # Search has a per-minute limit; GitHub says how long to wait.
            if err.code not in (403, 429) or attempt == 2 or "Retry-After" not in err.headers:
                raise
            time.sleep(min(int(err.headers["Retry-After"]), 90))
    return body.decode("utf-8", "replace") if accept.endswith(".raw") else json.loads(body)


def first_screenshot(readme: str, repo: str, branch: str, folder: str) -> str | None:
    """The first image in a README that looks like a screenshot rather than a badge or logo."""
    for m in README_IMAGE.finditer(readme):
        url = (m[1] or m[2]).strip()
        if NOT_SCREENSHOT.search(url) or not urllib.parse.urlparse(url).path.lower().endswith(SCREENSHOT_TYPES):
            continue
        if url.startswith("https://"):
            return url
        if "://" in url:
            continue
        path = posixpath.normpath(url.lstrip("/") if url.startswith("/") else posixpath.join(folder, url))
        return f"https://github.com/{repo}/raw/{branch}/{path}"
    return None


def cmd_refresh(_args) -> int:
    token = github_token()
    data = load_list()
    previous = load_metadata()
    repos = sorted({r for e in all_entries(data) if (r := entry_repo(e))})
    # README folders to look for screenshots in, per repository; entries with their own `screenshot` are skipped.
    folders: dict[str, set[str]] = {}
    for e in all_entries(data):
        if not e.get("screenshot") and (where := entry_readme(e)):
            folders.setdefault(where[0], set()).add(where[1])
    now = dt.datetime.now(dt.UTC)
    meta: dict = {}
    for repo in repos:
        try:
            info = github(f"/repos/{repo}", token)
        except urllib.error.HTTPError as err:
            if err.code != 404:
                raise
            meta[repo] = {"stars": 0, "status": "unavailable"}
            print(f"{repo}: unavailable", file=sys.stderr)
            continue
        pushed = dt.datetime.fromisoformat(info["pushed_at"])
        status = "archived" if info["archived"] else "inactive" if now - pushed > INACTIVE_AFTER else None
        meta[repo] = {"stars": info["stargazers_count"], "pushed": info["pushed_at"][:10], "status": status}
        shots = {}
        for folder in sorted(folders.get(repo, ())):
            path = f"/repos/{repo}/readme" + (f"/{urllib.parse.quote(folder)}" if folder else "")
            try:
                readme = github(path, token, accept="application/vnd.github.raw")
            except urllib.error.HTTPError as err:
                if err.code != 404:
                    # Keep the last known screenshot rather than dropping it over a hiccup.
                    if old := (previous.get(repo) or {}).get("screenshots", {}).get(folder):
                        shots[folder] = old
                    print(f"{repo}/{folder}: README fetch failed ({err.code})", file=sys.stderr)
                continue
            if url := first_screenshot(readme, repo, info["default_branch"], folder):
                shots[folder] = url
        if shots:
            meta[repo]["screenshots"] = shots
    METADATA.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(f"refreshed {len(repos)} repositories, {sum(len(m.get('screenshots', {})) for m in meta.values())} screenshots")
    return 0


# Searches cast a wide net; MARKERS decide what is really about Stencil's Tern.
# GitHub search matches substrings ("pattern plugin install", "stencil.so/terms"),
# and "tern" is also the old ternjs code-analysis engine.
DISCOVERY_REPO_QUERIES = [
    "topic:tern-plugin",
    "topic:stencil-tern",
    '"stencil.so/tern" in:readme',
    '"tern plugin install" in:readme',
    '"docs.stencil.so/tern" in:readme',
]
DISCOVERY_CODE_QUERIES = [
    '"tern.lens.define"',
    '"tern.block.define"',
    '"tern.chrome.status"',
    '"tern plugin install"',
    '"stencil.so/tern"',
]
MARKERS = re.compile(
    r"stencil\.so/tern\b|\btern plugin install\b|\btern\.(?:lens|block)\.define\b"
    r"|\btern\.chrome\.|Tern Surface Protocol|\bTERN_(?:DAEMON|WINDOW)_SOCKET\b"
)


def listed_repos(data: dict) -> set[str]:
    known = {os.environ.get("GITHUB_REPOSITORY", "theblazehen/awesome-tern").lower()}
    for e in all_entries(data):
        if repo := entry_repo(e):
            known.add(repo.lower())
        if m := re.match(r"^https://github\.com/([\w.-]+)/([\w.-]+)", e["url"]):
            known.add(f"{m[1]}/{m[2]}".lower())
    return known


def cmd_discover(args) -> int:
    """Print Tern repositories created in the last `--days` days that aren't listed.

    The window keeps reports short and stateless: anything not added simply ages out.
    """
    token = github_token()
    known = listed_repos(load_list())
    cutoff = dt.datetime.now(dt.UTC) - dt.timedelta(days=args.days)
    found: dict[str, dict] = {}
    failed: list[str] = []

    def add(repo: dict, query: str):
        name = repo["full_name"]
        if name.lower() in known or repo.get("fork"):
            return None
        hit = found.setdefault(name, {"repo": repo, "queries": [], "verified": False})
        hit["queries"].append(query)
        return hit

    for q in DISCOVERY_REPO_QUERIES:
        try:
            res = github(f"/search/repositories?per_page=100&q={urllib.parse.quote(q)}", token)
        except urllib.error.HTTPError as err:
            failed.append(f"{q} (HTTP {err.code})")
            continue
        for repo in res["items"]:
            add(repo, q)
    for q in DISCOVERY_CODE_QUERIES:
        time.sleep(7)  # code search allows about ten requests a minute
        try:
            res = github(
                f"/search/code?per_page=100&q={urllib.parse.quote(q)}", token,
                accept="application/vnd.github.text-match+json",
            )
        except urllib.error.HTTPError as err:
            failed.append(f"code: {q} (HTTP {err.code})")
            continue
        for item in res["items"]:
            fragments = " ".join(m.get("fragment", "") for m in item.get("text_matches", []))
            if MARKERS.search(fragments) and (hit := add(item["repository"], f"code: {q}")):
                hit["verified"] = True

    for name, hit in list(found.items()):
        try:
            # Code search results omit fork, stars and creation date.
            if "created_at" not in hit["repo"]:
                hit["repo"] = github(f"/repos/{name}", token)
            created = dt.datetime.fromisoformat(hit["repo"]["created_at"])
            if hit["repo"].get("fork") or created < cutoff:
                del found[name]
                continue
            if not hit["verified"]:
                readme = github(f"/repos/{name}/readme", token, accept="application/vnd.github.raw")
                if not MARKERS.search(readme):
                    del found[name]
        except urllib.error.HTTPError:
            del found[name]

    if failed:
        print("queries that failed: " + "; ".join(failed), file=sys.stderr)
    if found:
        print(f"Tern-related repositories created in the last {args.days} days that aren't on the list:\n")
        for name, hit in sorted(found.items(), key=lambda kv: -kv[1]["repo"].get("stargazers_count", 0)):
            r = hit["repo"]
            desc = (r.get("description") or "").strip() or "no description"
            print(
                f"- [{name}]({r['html_url']}) ★{r.get('stargazers_count', '?')}: {desc}"
                f" _(matched: {', '.join(sorted(set(hit['queries'])))})_"
            )
    return 0


# --------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check").set_defaults(func=cmd_check)
    sub.add_parser("build").set_defaults(func=cmd_build)
    sub.add_parser("refresh").set_defaults(func=cmd_refresh)
    p = sub.add_parser("discover")
    p.add_argument("--days", type=int, default=7, help="only report repositories created this recently")
    p.set_defaults(func=cmd_discover)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
