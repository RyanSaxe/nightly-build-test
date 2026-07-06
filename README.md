# The Nightly Build

*Built while you sleep.*

Scheduled AI agents research topics you choose and publish deep, cited, readable
**editions** to your own GitHub Pages library — courses that progress in order, daily
briefings, collections of deep dives. Any agent that can open a pull request can be
your night shift; CI (the **editor**) guarantees the site can never break.

**Status: phases 1–2 complete** (protocol, schemas, example series, and the proof —
`engine/check.py` — with a 50-case test suite). Phases 3–6 (site builder, templates,
skills, harness adapters, end-to-end) are specified in the handoff document.

## Layout
- `PROTOCOL.md` — the agent contract. Self-sufficient.
- `templates/registry.yaml` — what each template requires (length bands, sections,
  citation rules).
- `series/` — your series configs (two examples included).
- `engine/check.py` — the proof: BLOCK tier (publishing bar, CI-enforced) and WARN tier
  (quality bar, agent-iterated). Same tool in the agent loop and in CI.
- `.github/workflows/check.yml` — the editor: validates PRs to `library`, auto-merges
  clean ones, supersedes competitors.

## Try the proof
```
python3 engine/tests/make_fixtures.py
python3 engine/check.py engine/tests/fixtures/valid-dossier.html \
  --series semiconductors --repo . --today 2026-07-06
python3 engine/tests/run_tests.py
```
