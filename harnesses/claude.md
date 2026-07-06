# Harness adapter — Claude Code (Routines)

## 1. Connect

One-time: connect your fork at [claude.ai/code](https://claude.ai/code) →
add the GitHub repo. Grant access to the fork (contents + pull requests).
Claude Code Routines run in Anthropic's cloud — your laptop can be off.

## 2. Schedule

Create a Routine — in the Claude Code CLI type `/schedule`, or use
[claude.ai/code/routines](https://claude.ai/code/routines). Set the cadence
(nightly, e.g. `0 6 * * *` UTC for a 6:00 build) and paste the prompt below
with `<repo>` and `<series-id>` filled in.

Routines push work branches with default `claude/`-prefixed names — that's
fine; all protocol semantics live in the PR, not the branch name.

**Recommended: one Routine per series** (isolated failures, parallel nights).
Alternative: a single Routine whose prompt lists several series and instructs
one edition per series per run — simpler to manage, slower nights.

> You are the night shift for The Nightly Build repo `<repo>`. Work series:
> `<series-id>`. Read `PROTOCOL.md` on main and follow it exactly. Fallback
> summary: list `library/<series-id>/` on the `library` branch; pick the next
> unpublished item per `series/<series-id>/series.yaml`; research it deeply
> with cited sources; render ONE self-contained HTML file from the series
> template with the embedded `nb-meta` JSON block; run `python3 engine/check.py
> <file> --series <series-id>` and revise until BLOCK=0; open ONE pull request
> targeting the `library` branch adding ONLY `library/<series-id>/<slug>.html`,
> title `nb: <series-id>/<slug> — <Title>`, body containing the nb-meta yaml
> block. If nothing is unpublished, exit without a PR. Never modify other files.

## 3. Model

Pick the model when creating the Routine (settings on the routine). Deep
research rewards the strongest model you have access to — Fable/Opus-class for
longread templates (dossier, lesson, chronicle); Sonnet-class is serviceable
for briefs. The edition records whatever ran in `nb-meta.model` — your library
doubles as a model comparison corpus.

## 4. Verify

- Within the scheduled window, expect a PR titled `nb: <series>/<slug> — …`
  targeting `library`.
- The **Actions** tab shows the editor's verdict (`nightly-build-check`);
  clean PRs auto-merge, then `nightly-build-publish` rebuilds the site.
- First-run troubleshooting: repo not connected at claude.ai/code; the Routine
  lacks network access (enable web tools); the Routine ran but found no work
  (correct exit — check whether everything is already published); Pages not
  enabled (`./setup.sh`).
