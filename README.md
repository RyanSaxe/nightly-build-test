# The Nightly Build

*Built while you sleep.*

Fork one repo. Tell your AI agent **"set me up."** Paste one schedule prompt
into your harness. Every morning, open your phone to **tonight's build**:
deep, cited, beautifully rendered research editions on the things you want to
learn — published to your own GitHub Pages library, and delivered by feed or
morning email.

Over weeks this accumulates into a personal library: **courses** that progress
in order, ongoing **briefings**, **collections** of deep dives — permanent,
searchable, owned by you, served free from GitHub Pages.

- **Research, not summarization.** Editions are original cited research
  artifacts in six shipped layouts — dossier, lesson, brief, paper appraisal,
  chronicle, deck — plus [any template you invent](docs/customization.md).
- **Git as the protocol.** Any agent that can open a pull request can be your
  night shift — Claude Code, Jules, and Codex adapters ship in `harnesses/`.
- **A safety gate, not a quality gate.** CI (the **editor**) guarantees the
  site can never break; quality pressure happens inside the agent's loop via a
  repo-shipped checker (the **proof**). A missed night is worse than a thin
  edition.
- **One folder is yours.** All configuration — series, voice, themes,
  templates — lives in [`press/`](docs/press.md). Everything else is engine,
  so [engine updates are ordinary, clean git merges](docs/press.md).
- **Mobile first.** ~95% of reads happen on a phone; every surface is designed
  for one.

## Five-minute quickstart

1. **Fork** this repo, leaving GitHub's **"Copy the `main` branch only"** box
   checked — you get the engine and upstream's example configuration, never
   its library. (Private forks work too; Pages on private repos needs a paid
   plan.)
2. **Clone it and say "set me up"** to your agent in the checkout. Setup
   scaffolds your own `press/` — series, voice, title — and bootstraps the
   press (library branch, trigger workflows, Pages, auto-merge). Nothing is
   deleted: `press-example/` (upstream's live config) stays put as a working
   reference. Then enable workflows once in your fork's Actions tab. No agent
   handy? Run `./setup.sh` and edit `press/` by hand.
3. **Rehearse:** ask for a **press check** — a full research run rendered to
   a locally served newsstand, no PR, so you can tune prompts before
   scheduling.
4. **Schedule:** paste the one schedule prompt from your harness's adapter in
   `harnesses/`. **One nightly schedule for the whole press, ever** — each
   run derives its work list from the repo, so adding or finishing series
   never touches the schedule again.
5. **Sleep.** The night shift researches and opens one PR per series; the
   editor validates and merges; the press deploys; [the paperboy emails you
   the morning digest](docs/delivery.md) — or subscribe to `feed.xml`.

## How it works

| Piece | Where | What it does |
|---|---|---|
| `PROTOCOL.md` | main | The complete agent contract; self-sufficient |
| the proof | `engine/check.py` | Two tiers: BLOCK (publishing bar, CI-enforced) and WARN (quality bar, agent-iterated) — the same tool in both places |
| the editor | `check.yml` | Validates every PR to `library`; auto-merges clean ones; supersedes competitors |
| the press | `engine/build_site.py` + `publish.yml` | Rebuilds the site on every merge: newsstand, nightly builds, series pages, tags, search, Atom feeds, email digests |
| the paperboy | `morning-mail.yml` | Optional daily email of tonight's build ([setup](docs/delivery.md)) |
| templates | `templates/` (+ `press/templates/`) | Registry-defined layouts; user templates are first-class |
| skills | `skills/` | Librarian (setup, curation, engine updates) and Correspondent (the night shift runtime) |

**Source policy per series:** `required_docs` (committed files that must be
read *and* cited), `consult` (must-read starting points), and
`sources_exclusive` (editions may cite *only* the declared sources — enforced
by the proof).

**Security spine:** no executable logic ever lives on the `library` branch;
editions are sandboxed (no scripts beyond JSON data blocks and the engine's
own runtime, no iframes, no event handlers); the editor runs with read-only
contents and no secrets against untrusted diffs; auto-merge is squash-only,
into `library` only, for BLOCK-clean PRs only; mail credentials exist only as
Actions secrets on the trusted post-merge path.

## Docs

- [Your press: ownership, forks, clean updates](docs/press.md)
- [Customization: themes, voice, your own templates](docs/customization.md)
- [Delivery: feeds, morning email, the catalog API](docs/delivery.md)

## Try the engine locally

```
python3 engine/tests/run_tests.py        # proof + builder + end-to-end suites
python3 engine/validate_config.py        # validate press/ configuration
```

**This repo dogfoods itself.** `press-example/` is the upstream night
shift's real assignment sheet (the engine falls back to it when no `press/`
exists), so the maintainer's Pages site is a live demo of exactly what a
fork produces — and every config file in it is a working example.

MIT licensed. No accounts, no backend, no analytics — `catalog.json` and the
Atom feeds *are* the API.
