# Harness adapter — Jules (Google)

## 1. Connect

One-time: install the Jules GitHub app ([jules.google](https://jules.google))
and grant it access to your fork.

## 2. Schedule

Two options:

- **Native Scheduled Tasks** — in Jules, create a Scheduled Task on your fork
  with the prompt below and a nightly cadence.
- **jules-invoke GitHub Action** — use Google's official `jules-invoke` action
  as a thin cloud trigger from a one-line cron workflow in a *separate* repo or
  on `main` (never anything that runs on `library` PRs), passing the same
  prompt.

Fill `<repo>` and `<series-id>`. **One schedule per series** recommended; a
single task iterating multiple series also works (one edition per series per
run).

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

Jules selects its Gemini model tier from your plan; there is no per-task model
picker. Record honest provenance: the run should set `nb-meta.harness` to
`jules` and `nb-meta.model` to the model Jules reports.

## 4. Verify

- Expect a PR titled `nb: <series>/<slug> — …` targeting `library` in the
  window; Jules links the session from the PR.
- Actions tab → `nightly-build-check` for the editor's verdict; clean PRs
  auto-merge and `nightly-build-publish` deploys the site.
- First-run troubleshooting: app not installed on the fork; task created
  against the wrong branch (prompts reference `main` + `library` explicitly);
  no work available (correct silent exit); Pages not enabled (`./setup.sh`).
