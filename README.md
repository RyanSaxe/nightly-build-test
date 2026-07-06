# The Nightly Build

![The Nightly Build](assets/the-nightly-build-banner.png)

The Nightly Build is an engine for running a personal, AI-researched
newspaper. You fork this repository, describe what you want to read, and a
scheduled agent researches and publishes cited editions to your own GitHub
Pages site every night. Git is the entire protocol: any agent that can open
a pull request can be your night shift.

Editions are original research artifacts, not summaries. Five templates ship
with the engine (dossier, lesson, brief, paper appraisal, chronicle) and you
can define your own. Over weeks the nightly output accumulates into a
permanent, searchable library that you own and that GitHub serves for free.

## Quickstart

1. Fork this repository. Keep GitHub's "Copy the main branch only" box
   checked.
2. Clone your fork and tell your agent "set me up", or run `./setup.sh` and
   edit `press/` by hand. Setup scaffolds your configuration, creates the
   `library` branch, and enables Pages and auto-merge. Enable workflows once
   in your fork's Actions tab. A complete working configuration ships in
   `examples/` to copy from.
3. Rehearse. Ask your agent for a "press check": a full research run
   rendered to a locally served site, with no PR, so you can tune prompts
   before scheduling anything.
4. Schedule one nightly job for the whole press using the adapter for your
   harness in `harnesses/`. Each run derives its work list from the repo, so
   you never touch the schedule again.
5. Read. The night shift opens one PR per series, CI validates and merges,
   the site rebuilds, and the morning email or Atom feed delivers it.

## How it works

| Piece | Where | Purpose |
|---|---|---|
| `PROTOCOL.md` | main | The complete agent contract |
| the proof | `engine/check.py` | Validates editions. BLOCK findings stop publication; WARN findings drive revision |
| the editor | `check.yml` | Validates every PR to `library`, auto-merges clean ones, supersedes competitors |
| the press | `engine/build_site.py` | Rebuilds the site on every merge: front page, night archive, sections, search, feeds, email digests |
| the paperboy | `morning-mail.yml` | Optional daily email of the latest build |
| duty | `engine/duty.py` | Deterministic nightly work selection: cadence, pauses, completion, commissions |
| templates | `templates/` | Registry-defined layouts. User templates in `press/templates/` are first class |
| skills | `skills/` | Librarian (setup and curation) and Correspondent (the night shift runtime) |

Two branches with disjoint jobs: `main` holds the engine and your
configuration, `library` holds published editions and the generated site.
`press/` is the only directory you edit. It does not exist upstream, so
pulling engine updates is an ordinary merge with nothing to conflict.

## Configuration

Series live in `press/series/<id>/` as a `series.yaml` plus a prompt file.
Four modes: `collection` (an item list, published front to back or at
random), `sequence` (an ordered course), `rolling` (one edition per date),
and `open` (you describe a beat, the agent picks each night's topic and
form). Cadence, pausing, sections, source requirements, and quality bands
are one-line settings. See [docs/series.md](docs/series.md).

Sources can be constrained per series: `required_docs` are committed files
the agent must read and cite, `consult` lists must-read starting points, and
`sources_exclusive: true` restricts citations to the declared set. The proof
enforces all three.

## Security

No executable logic ever lives on the `library` branch. Editions are
sandboxed: no scripts beyond JSON data blocks and the engine runtime, no
iframes, no event handlers, and external references only to the engine
assets path and Google Fonts. The editor validates untrusted PRs with
read-only permissions and no secrets. Auto-merge is squash-only, into
`library` only, for BLOCK-clean PRs only. Mail credentials exist only as
Actions secrets on the trusted post-merge path.

## Development

The engine is Python 3.9+ with one dependency, PyYAML. Scripts carry PEP 723
metadata, so `uv run engine/check.py` works without any setup.

```
python3 engine/tests/run_tests.py    # proof, builder, and end-to-end suites
python3 engine/validate_config.py    # validate press/ configuration
```

This repository is engine-only. It runs no press and publishes no library;
the maintainer dogfoods by copying it like any other user. `examples/`
contains a complete working configuration as documentation.

## Docs

- [Your press: ownership, forks, updates](docs/press.md)
- [Series: modes, open desks, cadence, commissioning](docs/series.md)
- [Customization: themes, voice, your own templates](docs/customization.md)
- [Delivery: feeds, morning email, the catalog API](docs/delivery.md)

MIT licensed. No accounts, no backend, no analytics. `catalog.json` and the
Atom feeds are the API.
