# Harness adapter — Codex (OpenAI)

## 1. Connect

One-time: connect GitHub in Codex settings
([chatgpt.com/codex](https://chatgpt.com/codex) → Settings → GitHub) and grant
access to your fork. Codex cloud tasks run with the repo checked out.

## 2. Schedule

Codex's native automations currently run on your local machine, so for a
laptop-off nightly use a thin cloud trigger: a one-line cron workflow (in a
separate repo, or on `main`) that fires a Codex cloud task via the Codex API —
or an issue-label trigger if you prefer click-to-run. The trigger passes the
prompt below verbatim; all real behavior lives in `PROTOCOL.md`.

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

Choose the model/reasoning effort in Codex settings (or per task via the API
call). Deep research rewards the strongest tier; the edition records what ran
in `nb-meta.model` (`nb-meta.harness: codex`).

## 4. Verify

- Expect a PR titled `nb: <series>/<slug> — …` targeting `library` in the
  window.
- Actions tab → `nightly-build-check` for the editor's verdict; clean PRs
  auto-merge and `nightly-build-publish` deploys the site.
- First-run troubleshooting: GitHub not connected in Codex settings; the cloud
  environment lacks internet access (enable it in the Codex environment
  settings — research requires web); no work available (correct silent exit);
  Pages not enabled (`./setup.sh`).
