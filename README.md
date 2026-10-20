<!-- Generated from list.yml by tools/awesome_tern.py. Edit list.yml, not this file. -->

# Awesome Tern

> Plugins, apps, tools and resources for [Tern](https://stencil.so/tern), Stencil's terminal.

Tern is a Rust-native terminal from [Stencil](https://stencil.so). Shells, [omp](https://omp.sh) agents and browser panes keep running in a daemon when the window closes, and come back after a reboot. One session can be open on the desktop app, on iOS and in a WebGPU browser tab at the same time; typing in one shows up in the others.

Plugins are written in Luau, and any program can draw native UI through the Tern Surface Protocol (TSP). `tern remote serve` serves a remote machine's sessions over QUIC. Tern is in closed beta; you get in through the [waitlist](https://auth.stencil.so/waitlist?app=tern).

## Contents

- [Plugins](#plugins)
  - [Command lenses](#command-lenses)
  - [Blocks](#blocks)
  - [Window and workflow](#window-and-workflow)
  - [Official examples](#official-examples)
- [Native TSP apps](#native-tsp-apps)
- [Agent integrations](#agent-integrations)
- [SDKs and protocol libraries](#sdks-and-protocol-libraries)
- [Official resources](#official-resources)
  - [Documentation](#documentation)
- [Nix and dotfiles](#nix-and-dotfiles)

## Plugins

Tern plugins are written in Luau and can be installed directly from GitHub with `tern plugin install github.com/OWNER/REPO`. See the [plugin CLI reference](https://docs.stencil.so/tern/reference/cli.html) for the available commands.

### Command lenses

A lens captures a shell command's output and shows it as a native view. A Raw toggle shows the original text.

- [tern-kube](https://github.com/contrafy/tern-kube) ★ 7 · 2026-10-09 - Renders `kubectl` output as sortable, filterable native views, with a live Explore block, one-key pod shells and logs, previewed and confirmed changes, and GitOps drift against your manifests.
- [tern-jj](https://github.com/resYuto/tern-jj) ★ 2 · 2026-10-04 - Displays `jj status` and `jj st` output as a read-only native card with added, modified and deleted files colored to match the Tern theme.
- [tern-jj-diff](https://github.com/zsxawerdu/tern-jj-diff) ★ 1 · 2026-10-08 - Renders `jj diff` and `jj show` output as a native view with summary badges and one collapsible section per file, filling the gap left by Tern's built-in `jj st` and `jj log` views.

### Blocks

- [tern-grafana](https://github.com/contrafy/tern-grafana) ★ 7 · 2026-10-20 - Grafana and Prometheus-compatible backends as native blocks for PromQL queries, dashboards, alerts and silences, logs and traces; pre-release.
- [tern-pencil-preview](https://github.com/SamuelFontess/tern-pencil-preview) ★ 5 · 2026-10-17 - Previews pen.dev (Pencil) `.pen` designs in a block, rendering every top-level frame in one pen CLI run into a disk cache so switching frames is instant, with a layer list, an inspector and re-renders on save.
- [PR Guide](https://github.com/jubbydev/tern-pr-guide) ★ 4 · 2026-10-13 - Walks through a GitHub pull request one change at a time with the code beside a plain explanation, then lets you comment and post a single review.
- [tern-spotify](https://github.com/rico-vz/tern-spotify) ★ 4 · 2026-10-10 - Player block for the Spotify desktop app with cover art, playback, seeking and volume controls on macOS, Windows and Linux.
- [tern-spotify (Windows)](https://github.com/NaC-L/tern-spotify) ★ 4 · 2026-10-06 - Floating player for the Windows Spotify desktop app with cover art, playback controls, search, keyboard shortcuts and the current track in the status line.
- [tern-margin](https://github.com/Noctivoro/tern-margin) ★ 3 · 2026-10-08 - Renders a Markdown file block by block so you can leave CriticMarkup comments on any paragraph, list, table or code block, and hands them back to the agent that opened it.
- [tern-netsuite](https://github.com/contrafy/tern-netsuite) ★ 3 · 2026-10-09 - Native views for the NetSuite SuiteCloud SDF CLI with a production deploy guard, a project explorer and read-only SuiteQL execution logs and account health; public beta.
- [tern-office-preview](https://github.com/zerx-lab/tern-office-preview) ★ 3 · 2026-10-06 - Previews Word and Excel files natively in a block using a Rust renderer, with no Office, browser or LibreOffice involved.
- [tern-pokemon](https://github.com/ITSyndicate25/tern-pokemon) ★ 3 · 2026-10-08 - Ports vscode-pokemon to a block where Pokémon walk, sit and get petted on themed beach, forest and castle scenes, drawn natively with animated GIF sprites and no web view.
- [tern-video-block](https://github.com/verticalrectangle/tern-video-block) ★ 3 · 2026-10-05 - Opens video files in a block with mpv sound, frame stepping and synced side-by-side playback using ffmpeg and the kitty graphics protocol.
- [tern-ai-limits](https://github.com/pfTheTrial/tern-ai-limits) ★ 2 · 2026-10-20 - Side-column panel showing every usage window of your AI coding plans as a ring with its reset countdown, covering Claude, Codex, Cursor, Grok and anything omp tracks.
- [tern-CDP-tidal](https://github.com/H4vC/tern-CDP-tidal) ★ 2 · 2026-10-14 - Player block for the TIDAL desktop app, driven over the Chrome DevTools protocol, with cover art, playback, seeking, volume, shuffle, repeat and line-based search.
- [tern-pomodoro](https://github.com/tcstacks/tern-pomodoro) ★ 2 · 2026-10-09 - Minimal timer block with 25-minute focus and 5-minute break defaults, adjustable durations and a quiet progress line, using no network or subprocesses.
- [tern-rss](https://github.com/bmanturner/tern-rss) ★ 2 · 2026-10-13 - Follows RSS and Atom feeds in a block with expandable previews, articles in a docked reader browser, toasts for starred feeds and a catch-up line instead of an ever-growing unread count.
- [tern-ssh](https://github.com/aancw/tern-ssh) ★ 2 · 2026-10-09 - An ssh host manager that runs as a Tern pane. It lists the hosts of an ssh config, connects to them, and adds, edits and removes hosts without leaving Tern.
- [tern-todo](https://github.com/deLiseLINO/tern-todo) ★ 2 · 2026-10-17 - Task manager with tasks linked to terminal panes and agent sessions, kept in a JSON file and installable on remote hosts.
- [omp Tiles](https://github.com/MrsKugla/omp-tiles-plugin) ★ 1 · 2026-10-13 - Block with one colored tile per open omp session across all Tern sessions, showing the session title and whether it is working, waiting for you or idle.
- [Tern Reviewr](https://github.com/AxelMrak/tern-reviewr) ★ 1 · 2026-10-12 - Reviews staged, unstaged, and untracked Git changes in a native Tern diff view, sends line-anchored comments directly to an agent, and tracks per-file review progress.
- [tern-pr-tour](https://github.com/lfsmoura/tern-pr-tour) ★ 1 · 2026-10-16 - Step-by-step tours of a pull request that can answer questions inline, with a matching pr-tour agent skill.
- [tern-rmd](https://github.com/betizzel/tern-rmd) ★ 1 · 2026-10-17 - Opens R Markdown files as notebooks, running chunks in one live R session with plots and paged data frames shown under each chunk.
- [tern-software-factory](https://github.com/junaidrahim/tern-software-factory) ★ 1 · 2026-10-20 - Lists the agents on your Tern host and jumps to the pane of the one you select.
- [tern-spotify (kyle-elliott)](https://github.com/kyle-elliott/tern-spotify) ★ 1 · 2026-10-09 - Spotify player pane with album art, queue, library, search and device picker, plus a floating mode, status-line track and palette commands for playback.
- [tern-tracker](https://github.com/foxzool/tern-tracker) ★ 1 · 2026-10-14 - Lists the GitHub issues and pull requests of the repository in the focused pane's directory, with comments and a form for creating issues, in English or Chinese.
- [TernMeOn](https://github.com/segmentationf4u1t/Tern-Me-On) ★ 1 · 2026-10-08 - Controls Buttplug devices from Tern, with haptic patterns written as code and feedback when long commands finish.
- [Carly Switch](https://github.com/zyzhou-s-lab/carly-switch) ★ 0 · 2026-10-15 - Switches Carly's native realtime voice between Doubao and OpenAI from a compact panel, including a connection test that does not start the microphone.
- [Forge Meetings](https://github.com/Moti-Velz/tern-forge/tree/main/meetings) ★ 0 · 2026-10-13 - Lists Granola and Fireflies meetings, email threads over IMAP and local transcript exports in one keyboard-driven block, and pastes the ones you pick into the agent's composer as a summary or full transcript.
- [kedi-tern](https://github.com/kedi-lang/kedi-tern) ★ 0 · 2026-10-09 - Read-only viewer for `.kedi` files that highlights them in a native Tern editor using tree-sitter, without running the embedded Python.
- [tern-annotate](https://github.com/hyper-stition/tern-annotate) ★ 0 · 2026-10-13 - Prototype for commenting on a snapshot of any block and sending the edit comments to an agent in batches.
- [tern-bigquery](https://github.com/junaidrahim/tern-bigquery) ★ 0 · 2026-10-15 - BigQuery browser built on the `bq` tool, with project search, dataset and table navigation, schema inspection and scrollable data previews.
- [tern-canvas-viewer](https://github.com/iacore/tern-canvas-viewer) ★ 0 · 2026-10-16 - Opens `.excalidraw` and `.tldraw` drawings as a rendered picture in a block instead of their JSON source.
- [tern-csv](https://github.com/taooceros/tern-csv) ★ 0 · 2026-10-13 - Shows CSV and TSV files as a native keyboard-driven table with a Table and Text switch.
- [tern-dbgview](https://github.com/Hime7864/tern-dbgview) ★ 0 · 2026-10-14 - Shows Windows debug output as it is produced, from kernel-mode `DbgPrint` and user-mode `OutputDebugString`.
- [tern-difftastic](https://github.com/MicroProofs/tern-difftastic) ★ 0 · 2026-10-20 - Reviews jj and git changes as difftastic's structural side-by-side diffs in a block, with search across both sides of every file and seen and reviewed marks on hunks that survive rebases.
- [tern-find-in-files](https://github.com/jmilldotdev/tern-find-in-files) ★ 0 · 2026-10-13 - VS Code-style search across the files under a folder, powered by ripgrep, with results updating as you type.
- [tern-omp-stats](https://github.com/BaLaurent/tern-omp-stats) ★ 0 · 2026-10-17 - Dashboard block built from native components that turns the usage statistics in `~/.omp/stats.db` into per-model and per-project tables with cost.
- [tern-periscope](https://github.com/kenXengineering/tern-periscope) ★ 0 · 2026-10-16 - Lists the subagents of an omp session with live status, tool counts and cost, and opens any transcript as it is written.
- [tern-ports](https://github.com/meisijiya/tern-ports) ★ 0 · 2026-10-19 - Shows every listening TCP port on your machine and marks the ones an omp process started.

### Window and workflow

Window plugins add commands, keybindings, layouts, and status-line segments.

- [tern-agent-scheduler](https://github.com/bmanturner/tern-agent-scheduler) ★ 18 · 2026-10-17 - Schedules omp agent runs with cron, presets, plain-English or one-shot times, starts each in a background tab and keeps their results, failures and costs in a manager block, with status-line, notification and Carly support.
- [Overseer](https://github.com/mmnavarr/overseer) ★ 11 · 2026-10-14 - Panel listing every branch in flight with its worktree, agents, pull request and ticket, where each worktree gets its own Tern session.
- [tern-projects](https://github.com/thegeneralist01/tern-projects) ★ 8 · 2026-10-16 - Curated multi-folder projects, pinned chats, and search across OMP, Claude Code, Codex, Pi, OpenCode, and Cursor.
- [omaterm](https://github.com/betizzel/omaterm) ★ 6 · 2026-10-06 - Matches Tern's background, foreground, window chrome and ANSI colors to your active Omarchy theme.
- [tern-cat](https://github.com/contrafy/tern-cat) ★ 6 · 2026-10-16 - Adds a pixel-art menace that naps in your panes, swats at your pointer, stares when you sudo and dives through portals when you switch panes.
- [tern-herdr](https://github.com/safzanpirani/tern-herdr) ★ 5 · 2026-10-06 - Shows Herdr as native Tern tabs, splits and a sidebar, with tabs colored by agent state and Herdr's prefix keys working.
- [workspaces-sidebar](https://github.com/rezhajulio/workspaces-sidebar) ★ 5 · 2026-10-13 - Pins a workspace sidebar to every tab that lists sessions and their tabs as a tree, with live badges for waiting agents, running and failed commands, one-click switching, tab color tags, and attention-jump keybindings.
- [herdr-tern-plugin](https://github.com/gabrielmoreira/herdr-tern-plugin) ★ 3 · 2026-10-05 - Adds an Open Herdr Session command that picks an existing herdr session and attaches to it inside Tern without copying or converting workspaces.
- [tern-chirp](https://github.com/Noctivoro/tern-chirp) ★ 3 · 2026-10-08 - Plays a short synthesized beep when an agent finishes or waits for you, with the sound's shape chosen by Jev to match how the turn went.
- [tern-mizu](https://github.com/ITSyndicate25/tern-mizu) ★ 3 · 2026-10-08 - Paints the Mizu Icons VS Code file icon theme over the Files pane, with 893 icons covering 847 file names, 947 extensions and 1457 folder names.
- [tern-plugin-omp-usage](https://github.com/jmazzola/tern-plugin-omp-usage) ★ 3 · 2026-10-14 - Shows omp usage limits above the composer's context bar, with a meter, reset countdown and clock time for each window on hover.
- [tern-usage-monitor](https://github.com/rico-vz/tern-usage-monitor) ★ 3 · 2026-10-06 - Floating or docked panel showing usage for every omp linked account, with per-account quota bars, auto-refresh, ordering and update-time settings.
- [tern-worktree](https://github.com/nibblebot/tern-worktree) ★ 3 · 2026-10-09 - Lists, opens and creates git worktrees from the command palette using plain git, with `jq` and a POSIX shell as the only other requirements.
- [CodexBar AgentView](https://github.com/materemias/codexbar-agentview) ★ 2 · 2026-10-16 - Shows Claude, Codex and other AI provider usage from the CodexBar CLI in the status line, with a dashboard that lists live and ended Claude Code, Codex, omp and pi sessions and focuses or resumes them in Tern tabs.
- [tern-chime](https://github.com/H4vC/tern-chime) ★ 2 · 2026-10-08 - Plays a configurable sound when a pane raises an unseen alert, an omp agent yields its turn, or a long command finishes, with bundled chimes and per-trigger overrides.
- [tern-haptic-alert](https://github.com/lfsmoura/tern-haptic-alert) ★ 2 · 2026-10-06 - Sends a haptic pulse to a Logitech MX Master 4 when an agent finishes or is blocked waiting for input.
- [tern-ide layout](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/layout.nix) ★ 2 · 2026-10-19 - Window plugin with an IDE-style four-pane layout, set split ratios, and an omp pane, packaged with Nix inside a NixOS config.
- [tern-jj workspaces](https://github.com/plumj-am/nixos/blob/master/packages/tern-plugins/jj.nix) ★ 2 · 2026-10-19 - Creates, opens, removes, and inspects jj workspaces using Tern dialogs, tabs, and the status line, packaged with Nix inside a NixOS config.
- [tern-plugins (Yupmoh)](https://github.com/Yupmoh/tern-plugins) ★ 2 · 2026-10-16 - Collection whose Kai plugin is a workspaces sidebar showing each session as a card with its agents, files, git changes and branches.
- [tern-remote-open](https://github.com/LoneExile/tern-remote-open) ★ 2 · 2026-10-13 - Opens file links, localhost URLs and OAuth loopback sign-in links from remote ssh panes on your Mac, where the file or port would not otherwise exist.
- [tern-vscode-dark](https://github.com/ITSyndicate25/tern-vscode-dark) ★ 2 · 2026-10-15 - Paints Tern with VS Code's Dark Modern theme, covering window chrome, terminal colors and the file editor's syntax colors.
- [tern-zh-cn](https://github.com/maicent/tern-zh-cn) ★ 2 · 2026-10-14 - Partial Simplified Chinese translation with Chinese titles for over 50 built-in palette commands and CSS replacement of the palette tabs and tab-bar buttons.
- [Toons](https://github.com/TazeDiB/Toons-Tern) ★ 2 · 2026-10-08 - Draws cartoons of what the agent is doing while commands run, as a port of claude-toons to Tern's native UI.
- [pane-highlight](https://github.com/olegpulatov/pane-highlight) ★ 1 · 2026-10-11 - Marks the active split with a border and tint, dims the others, and recolors a pane by user or host, such as red for `prod-*` hosts.
- [tern-agents](https://github.com/maxtuzz/tern-agents) ★ 1 · 2026-10-08 - Runs Claude Code, Codex, Gemini, OpenCode, Aider or any agent CLI as a Tern agent block, with profiles, run presets, a launcher and an Agents sidebar.
- [tern-bell](https://github.com/qiaoqinyu/tern-bell) ★ 1 · 2026-10-12 - Rings a bell when an agent turn finishes, with a keyboard-driven settings pane that previews fourteen macOS system sounds and user-supplied custom sounds before saving.
- [tern-file-paste](https://github.com/vokativ/tern-file-paste) ★ 1 · 2026-10-13 - Uploads copied local files from macOS, Linux, and Windows to remote hosts over SSH and inserts their paths into Tern panes.
- [tern-git-fx](https://github.com/willstarnet/tern-git-fx) ★ 1 · 2026-10-13 - Plays a small pixel-art animation in the pane corner while a git command runs, then a success or failure ending based on its exit status.
- [tern-model-usage](https://github.com/azmifarih/tern-model-usage) ★ 1 · 2026-10-04 - Shows omp coding-plan quota for each signed-in account in the status line and opens a canvas pane with provider cards and reset countdowns.
- [tern-omp-usage](https://github.com/joaodutra88/tern-omp-usage) ★ 1 · 2026-10-19 - Shows Claude and Codex limits from omp in the status line as colored dots, with a Monday-to-Friday weekly budget, saved resets and today's tokens and API cost.
- [tern-plugins (Unravl)](https://github.com/Unravl/tern-plugins) ★ 1 · 2026-10-15 - Collection with a left sidebar of sessions per host that shows omp agent status, and a fix that keeps the omp composer bar one band when macOS Reduce transparency is on.
- [tern-status](https://github.com/getpipher/tern-status) ★ 1 · 2026-10-06 - Status line in the style of tmux with CPU, memory, battery, network, disk and clock segments drawn with Tern's own icons and theme tones.
- [tern-tab-status](https://github.com/yoyooyooo/tern-tab-status) ★ 1 · 2026-10-17 - Colors tabs by whether their omp and pi sessions are working, waiting or need your attention.
- [tern-worktrees](https://github.com/riicodespretty/tern-worktrees) ★ 1 · 2026-10-13 - Opens git worktrees as Tern tabs with a branch picker and teardown on close, backed by a `tern-wt` CLI and an omp skill for agents.
- [tern-worktrees (aliefe04)](https://github.com/aliefe04/tern-worktrees) ★ 1 · 2026-10-07 - Adds palette commands that create a git worktree on a new branch with an agent tab, and remove the focused worktree only when it is clean and merged into the default branch.
- [TernGitButler](https://github.com/edheltzel/GitButler-for-Tern) ★ 1 · 2026-10-19 - GitButler workspaces in Tern, with a status-bar segment, a workspace block with one lane per branch stack and a diff block.
- [Worktree Panel](https://github.com/mullerino/tern-worktree-panel) ★ 1 · 2026-10-16 - Pins a panel to every tab that lists the git worktrees of the focused repository with the state of the omp agents in each, moves agents waiting for you to the top, and focuses or opens a worktree's tab on click.
- [font-default](https://github.com/getpipher/font-default) ★ 0 · 2026-10-06 - Makes the Reset font size command return to your configured size instead of Tern's built-in default.
- [Forge Omarchy](https://github.com/Moti-Velz/tern-forge/tree/main/omarchy) ★ 0 · 2026-10-13 - Makes Omarchy's window keys act on Tern panes first and fall through to Hyprland at the edges, in the style of vim-tmux-navigator, with desktop notifications when agents finish or wait for you.
- [Forge Projects](https://github.com/Moti-Velz/tern-forge/tree/main/projects) ★ 0 · 2026-10-13 - Sidebar for parallel agent work that gives each git worktree its own Tern session, with agent status, pull request and Linear ticket on every row, and one box that opens or creates a worktree from a branch, ticket or pull request.
- [jira-tern](https://github.com/hanbong5938/jira-tern) ★ 0 · 2026-10-13 - Native Jira browser that reads and posts issue comments, runs status transitions, and opens a Git worktree or jj workspace with an omp agent tab for an issue.
- [power-surge](https://github.com/dbydd/power-surge) ★ 0 · 2026-10-11 - Neovim plugin that shows sparks on every text change with a combo meter and screen shake, with a Tern command and chord for it.
- [remote-image-paste](https://github.com/zyzhou-s-lab/remote-image-paste) ★ 0 · 2026-10-13 - Uploads a macOS clipboard image to the focused remote host over SSH and pastes the server path into the current pane.
- [tern-agent-progress](https://github.com/Sipty/tern-agent-progress) ★ 0 · 2026-10-11 - Marks tabs that run omp agents with WoW-style quest marks and todo progress bars.
- [tern-browser-profiles](https://github.com/ian139/tern-browser-profiles) ★ 0 · 2026-10-15 - Opens a Chrome, Brave or Edge profile on macOS inside Tern as an isolated browser signed in with that profile's cookies.
- [tern-claude-usage](https://github.com/zerx-lab/tern-claude-usage) ★ 0 · 2026-10-12 - Shows Claude Pro and Max usage limits in a panel and a status-line segment, with 5-hour and 7-day windows, per-model limits, pace tracking and reset countdowns.
- [tern-close-plugin](https://github.com/yumosx/tern-close-plugin) ★ 0 · 2026-10-05 - Adds palette commands that close the other tabs and the split blocks left, right and around the focused block, each row hidden while it would close nothing.
- [tern-custom-background](https://github.com/naraaalt/tern-custom-background) ★ 0 · 2026-10-13 - Puts a dithered picture behind the whole window, with a settings page to pick the image and how it is drawn.
- [tern-desktop-pet](https://github.com/hanbong5938/tern-desktop-pet) ★ 0 · 2026-10-19 - Connects Tern agent observations and semantic asks to the separately installed Desktop Pet app.
- [tern-extrakeys](https://github.com/bneil/tern-extrakeys) ★ 0 · 2026-10-17 - Termux-style bar of buttons for Esc, Ctrl, Alt, Tab, arrows and more that types into a pane you choose, using Termux's extra-keys config format.
- [tern-gpg-touch](https://github.com/edcnogueira/tern-gpg-touch) ★ 0 · 2026-10-14 - Shows a toast, and optionally plays a sound, when a typed command starts that will wait for a touch on your GPG security key, with per-folder rules.
- [tern-grid-layout](https://github.com/yoyooyooo/tern-grid-layout) ★ 0 · 2026-10-17 - Arranges the panes of a tab into equal-width columns when the window resizes or on request, keeping manual divider changes in between.
- [tern-kami](https://github.com/justdoswift/tern-kami) ★ 0 · 2026-10-16 - Warm-paper theme with parchment backgrounds, ink-blue accents and serif type, inspired by Kami.
- [tern-minimax-quota](https://github.com/meisijiya/tern-minimax-quota) ★ 0 · 2026-10-19 - Shows your MiniMax Token Plan quota in the status line and refreshes it every five minutes.
- [tern-obsidian](https://github.com/dbydd/tern-obsidian) ★ 0 · 2026-10-19 - Recognizes Obsidian vaults and opens their notes, Bases and JSON Canvas files in native reader blocks.
- [tern-omp-groups](https://github.com/vishiod/tern-omp-groups) ★ 0 · 2026-10-19 - Groups omp chats by the code at the start of their titles and lists every saved chat under its group, reopening a closed one in that group with a click.
- [tern-omp-layout-fixes](https://github.com/0xGREG/tern-omp-layout-fixes) ★ 0 · 2026-10-09 - Widens omp transcripts to the full pane and adds spacing above the composer, touching only omp session surfaces.
- [tern-paste-image](https://github.com/Microck/tern-paste-image) ★ 0 · 2026-10-10 - Pastes Windows clipboard screenshots into local or remote Tern terminals with Ctrl+Alt+V, uploading over SSH and inserting the quoted path without pressing Enter.
- [tern-plugins (mreishus)](https://github.com/mreishus/tern-plugins) ★ 0 · 2026-10-17 - Collection of small plugins, including one that moves the tab bar to the bottom in the tiles, studio and float layouts and one that opens a pane's scrollback in nvim.
- [tern-remote-paste](https://github.com/jmilldotdev/tern-remote-paste) ★ 0 · 2026-10-13 - Makes Ctrl+V in an ssh pane upload a Mac clipboard image to the remote host and paste its path for agents such as omp and Claude Code.
- [tern-swarm](https://github.com/bmanturner/tern-swarm) ★ 0 · 2026-10-06 - Kanban board that runs omp agents on its cards in separate git worktrees, runs your checks on their work and waits for your approval.
- [tern-task-plugin](https://github.com/yesmeck/tern-task-plugin) ★ 0 · 2026-10-13 - Makes each task a session with its own branch, git worktree and default agent, with a kanban dashboard of pull request status.
- [tern-vimnav](https://github.com/mayask/tern-vimnav) ★ 0 · 2026-10-08 - Brings vim-tmux-navigator to Tern so Ctrl+H/J/K/L moves between Neovim splits and Tern panes.
- [tern-workspaces-sidebar](https://github.com/tobiasesquivel/tern-workspaces-sidebar) ★ 0 · 2026-10-14 - Sidebar that lists every session as a workspace with nested tabs, git counters and agent state, plus a small runtime that gives omp, Claude Code and Codex the same status.

### Official examples

These examples ship with the official [SDK repository](https://github.com/stencil-hq/tern-sdk). They are a good starting point if you are writing your own plugin.

- [Terraform Plans](https://docs.stencil.so/tern/examples/terraform.html) - Lens for `terraform plan` and `tofu plan` that shows badges, diagnostics and resources grouped by action.
- [Review Queue](https://docs.stencil.so/tern/examples/review-queue.html) - Block that polls `gh` every two minutes and lists pull requests waiting for your review.
- [JSON Explorer](https://docs.stencil.so/tern/examples/jsonx.html) - Opens JSON and GeoJSON files as collapsible trees and copies the jq path of a node.
- [Long-Running Commands](https://docs.stencil.so/tern/examples/longrun.html) - Shows a toast when slow commands finish, keeps a history of run times and status, and adds a status-line segment.
- [Directory Variables](https://docs.stencil.so/tern/examples/dirvars.html) - Loads approved `.tern-env` files into new shells and signals when a directory's environment changed.
- [Project Workspaces](https://docs.stencil.so/tern/examples/workspaces.html) - Builds named tabs and split panes from `.tern/workspace.json`.
- [Canvas Dashboard](https://docs.stencil.so/tern/reference/api-window.html#canvas-cx) - Window-only persistent dashboard that shows canvas ownership, keyed patches, and a Refresh action.

## Native TSP apps

Applications that draw their own user interface natively inside Tern using the Tern Surface Protocol (TSP).

- [oh-my-pi (omp)](https://github.com/can1357/oh-my-pi) ★ 36041 · 2026-10-20 - Stencil's coding agent that Tern is built around, drawing its transcript and UI natively, restoring sessions, and opening web pages as browser picture-in-picture panes.
- [Hermes for Tern](https://github.com/thefullctx/hermes-for-tern) ★ 18 · 2026-10-10 - Unofficial Tern frontend for Hermes Agent that draws the conversation, tool rows, subagents, buttons and a docked composer natively over TSP, and leaves the normal Hermes interface alone in other terminals.
- [rmon](https://github.com/pgkt04/rmon) ★ 9 · 2026-10-18 - Resource monitor for Linux and macOS with CPU, GPU, memory, network, disk and process panels and a disk benchmark, drawn natively in Tern over TSP.
- [neotern](https://github.com/arg3t/neotern) ★ 7 · 2026-10-07 - Neovim drawn as a native Tern surface in the style of Neovide, with a native command palette and picker; alpha and tuned to the author's own dotfiles.
- [Octet](https://github.com/skaft-software/octet/pull/485) ★ 7 · 2026-10-20 - Coding-agent shell rendering transcript cards, split diffs, pickers, and reports through TSP; Tern support is merged into the integration branch for 0.8.2 but not in the latest 0.8.1 release.
- [mantern](https://github.com/theblazehen/mantern) ★ 6 · 2026-10-05 - Drop-in `man` replacement that draws pages natively in Tern over TSP, with a synopsis card, option cards, tables, foldable sections and clickable SEE ALSO links, and falls back to the system `man` elsewhere.
- [Ternatro](https://github.com/verusferro/Ternatro) ★ 3 · 2026-10-09 - Plays Balatro in a Tern pane, running the game's own Lua code from your copy of Balatro.exe and drawing its layout, card motion, particles and shaders natively; you need to own the game.
- [saavy](https://github.com/saavy1/saavy_cloud) ★ 2 · 2026-10-05 - Persistent coding agent on Cloudflare with a native TSP frontend in Tern and a `pi-tui` fallback elsewhere.
- [tern-kata](https://github.com/Dangerboi/tern-kata) ★ 2 · 2026-10-19 - Browses and edits kata issues in a native pane opened with F9 or the palette, with Markdown issue bodies, priority and label chips, and kata links from agent chat that open the issue.
- [Terngram](https://github.com/d3d0n/terngram) ★ 2 · 2026-10-05 - Unofficial keyboard-driven Telegram client built on TDLib and omp's UI toolkit, also installable as a Tern plugin.

## Agent integrations

- [omp-side](https://github.com/wolfiesch/omp-side) ★ 9 · 2026-10-12 - Adds a `/side` command to fork the conversation into a child session and open it in a side pane in Tern, cmux, tmux, WezTerm, Kitty, and Ghostty.
- [pi-tern](https://github.com/Ghost-9/pi-tern) ★ 5 · 2026-10-07 - Makes the pi coding agent Tern-aware with the TSP handshake, native Mermaid diagrams, browser automation, pane capture and a session mirror.
- [tern-awui](https://github.com/materemias/tern-awui) ★ 2 · 2026-10-20 - Phone and browser web app for the omp agents running in Tern, reached over Tailscale, with sessions grouped by project and two-way control for prompts, questions, model choice, rewind and push notifications.
- [tern-mcp](https://github.com/NaC-L/tern-mcp) ★ 2 · 2026-10-03 - Python MCP server over stdio wrapping the tern CLI with 14 tools for sessions, panes, capture, process inspection, input and layout.
- [omp-thinking-translator](https://github.com/Mouriya-Emma/omp-thinking-translator) ★ 1 · 2026-10-14 - An omp extension that translates visible thinking into collapsible native sections in Tern and plain ANSI output in other terminals.
- [tern-control](https://github.com/wolfiesch/tern-control) ★ 1 · 2026-10-01 - An omp and Pi extension giving agents tools to find Tern sessions, read transcript digests, follow daemon events, change layout, and type into terminals.
- [grokbot-bridge](https://github.com/cangiolo/grokbot-bridge) `unavailable` - Connects Grok Bot with interactive omp sessions in Tern through live composer status widgets, subtask stopwatch beacons, and prompt header session claims.
- [tern-omp-vimnav](https://github.com/DinMon/tern-omp-vimnav) ★ 0 · 2026-10-07 - Vim-style navigation of the omp transcript in Tern, with block cursor, text selection and copying, search and Vimium-style hints for links, code blocks and buttons.

## SDKs and protocol libraries

- [tern-sdk](https://github.com/stencil-hq/tern-sdk) ★ 68 · 2026-10-19 - Official repository of Surface Protocol SDKs for Rust, Python, Go and TypeScript, plus the Luau type definitions (`tern.d.luau`) and example plugins.
- [@oh-my-pi/pi-wire](https://github.com/can1357/oh-my-pi/tree/main/packages/wire) ★ 36041 · 2026-10-20 - TypeScript package implementing the TSP wire format: APC framing, component types, frame operations, handshake and events.
- [@oh-my-pi/pi-tui](https://github.com/can1357/oh-my-pi/tree/main/packages/tui) ★ 36041 · 2026-10-20 - TypeScript UI toolkit from omp for rendering transcripts, chat, dashboards, and pickers natively over TSP.
- [octet-tern](https://github.com/skaft-software/octet/tree/9e8abda1f4f210d43361b6c0a80e482097feff77/crates/octet-tern) ★ 7 · 2026-10-20 - A Rust TSP client built into Octet with wire types, APC chunking, tty flow control, and scene builders.

## Official resources

- [Tern](https://stencil.so/tern) - Stencil's product page for Tern with a feature tour.
- [Waitlist](https://auth.stencil.so/waitlist?app=tern) - Sign up for Tern's closed beta using a Stencil account.
- [Beta builds](https://build.stencil.so/tern) - CI-generated beta builds from the `main` branch, requiring sign-in.
- [Stencil on GitHub](https://github.com/stencil-hq) - Stencil's GitHub organization; Tern's source is not public.
- [@stencil_labs](https://x.com/stencil_labs) - Stencil's account on X.
- [@_can1357](https://x.com/_can1357) - Stencil founder Can Bölük on X, where he posts most Tern announcements.
- [omp Discord](https://discord.gg/4NMW9cdXZa) - The community Discord server for omp, where Tern is also discussed.

### Documentation

- [Tern plugin book](https://docs.stencil.so/tern/) - Official documentation covering host and window runtimes, lenses, blocks, native views, styling, and TSP.
- [Getting Started](https://docs.stencil.so/tern/guides/getting-started.html) - Walkthrough of building a lens and palette command, then linking, type-checking, and reloading.
- [Command Lenses](https://docs.stencil.so/tern/guides/lenses.html) - Explains how to turn command output into native views using manifest globs and host callbacks.
- [Debugging](https://docs.stencil.so/tern/guides/debugging.html) - Covers toasts, logs, Luau typing, handler budgets, and scripted window control.
- [Plugin CLI](https://docs.stencil.so/tern/reference/cli.html) - Reference for `tern plugin list`, `install`, `link`, `unlink`, `remove`, `reload`, `dir`, and `types`.
- [Tern Surface Protocol](https://docs.stencil.so/tern/protocol/index.html) - Specifies the in-band protocol where CLIs, TUIs, and agents send UI trees that Tern lays out and draws natively.

## Nix and dotfiles

Tern builds are behind a sign-in, so these Nix setups expect you to download the build yourself.

- [pelikanade/flake](https://github.com/pelikanade/flake/blob/f6f8217278a4a119c8e3a5b27b5a30ffef57cbd1/docs/tern.md) ★ 11 · 2026-10-20 - Nix packaging guide covering signed-in downloads, `requireFile`, graphics libraries, and updating.
- [plumj-am/nixos](https://github.com/plumj-am/nixos/blob/master/modules/tern.nix) ★ 2 · 2026-10-19 - NixOS module that manages Tern settings, theme, tmux-style keybindings, the `omp` launch command and plugins.
- [tdortman/dotfiles](https://github.com/tdortman/dotfiles/tree/008242f1f3ef305950a98f9878a0253477f256b0/nix) ★ 1 · 2026-10-18 - A Nix package with desktop entries, an update script finding new builds via a Stencil browser session, and a KDE Plasma Home Manager module where Meta+Return focuses Tern or starts it.
- [theoparis/nix-tern](https://github.com/theoparis/nix-tern) ★ 1 · 2026-10-07 - Nix flake that packages a hand-downloaded Tern tarball and keeps it from being garbage collected.

## Contributing

Suggestions are welcome as pull requests. Read the [contribution guidelines](CONTRIBUTING.md) first.
