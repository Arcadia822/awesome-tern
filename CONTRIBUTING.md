# Contributing

Thanks for helping out. Only add things related to [Stencil's Tern](https://stencil.so/tern); other projects called "tern" don't belong here.

## Adding an entry

Edit `list.yml` and open a pull request. Don't edit `README.md`; it's regenerated from `list.yml` after your PR is merged.

Add the entry under the section where it fits:

```yaml
    - name: tern-jj
      url: https://github.com/resYuto/tern-jj
      kind: plugin
      description: Renders `jj status` as a read-only, color-coded card inside Tern.
```

- `kind` says what the thing is:
  - `plugin`: a Luau plugin installed with `tern plugin install`.
  - `app`: a standalone program that draws its UI in a Tern pane over the Tern Surface Protocol.
  - `extension`: runs inside a coding agent, such as an omp or pi extension or an MCP server.
  - `companion`: runs outside Tern, such as a web, mobile or desktop client.
  - `library`: an SDK or protocol library.
  - `config`: a Nix package or module, or dotfiles.
  - `docs`: documentation.

  If a project is more than one of these, pick the one most people will use.
- `description` is one plain sentence that starts with a capital letter and ends with a period. Don't repeat the name.
- Most sections are sorted by GitHub stars, so the position you pick doesn't matter there. Sections marked `sort: manual` keep the order in the file.
- If the link points into a repository (a file in someone's dotfiles, say), add `repo: owner/name` so the entry gets stars and status.
- Entries get a "Screenshot" dropdown automatically when the project's README has a screenshot (the first PNG, JPG, GIF or WebP that isn't a badge, logo or banner). To pick a different image, add `screenshot: https://…`; to turn it off, add `screenshot: none`.
- Social posts and videos go stale quickly, so they don't belong here.

### Choosing a section

Sections are grouped by what a project is for, not how it's built, and each entry appears once. Put it where a reader would look for it first; we'll move it if needed.

- **Integrations** is for projects that exist to make Tern fit a setup you already work in: a multiplexer, editor, window manager or browser. If the other tool is only a source of data (notes, music, clusters, tickets), use the section for what the project shows instead.
- If nothing fits, use **Other**. If you think a new section is needed, open an issue first.

CI checks the format of `list.yml` on every pull request. To check locally, run `mise run check`.

## What the automation does

- **CI** validates `list.yml` on pull requests. When changes land on `main`, and again every night, it fetches stars and last-push dates, re-sorts sections, marks entries `archived`, `inactive` (no push in six months) or `unavailable`, and regenerates `README.md`.
- **Links** checks every link weekly and opens an issue when something breaks.
- **Discover** searches GitHub weekly for Tern projects created that week that aren't listed, and posts them to a review issue.
