# Morning delivery — feeds, email, and the catalog API

## Feeds (zero setup — this works today)

Every press publishes Atom feeds:

- `https://<you>.github.io/<repo>/feed.xml` — the whole press
- `https://<you>.github.io/<repo>/series/<id>/feed.xml` — one series

Subscribe in any reader, or recreate morning email delivery with an
RSS-to-email service (Feedrabbit, Blogtrottr, Kill the Newsletter) — no
secrets, no configuration in the repo.

## The morning email (opt-in)

The press builds a designed, inline-styled email digest of every night's
build — headline, dek, and reading time per edition, with a procedural
summary line ("6 editions · 78 minutes of reading"). The **paperboy**
workflow (`morning-mail.yml`) delivers the latest digest once per day.

Enable it with two steps:

1. **Pick a send hour** in `press/site.yaml`:

```yaml
email:
  send_utc_hour: 12    # 12:00 UTC ≈ 8am ET / 5am PT
```

2. **Add repo Actions secrets** (Settings → Secrets and variables → Actions):

| Secret | Example |
|---|---|
| `MAIL_TO` | `you@example.com` |
| `MAIL_FROM` | `The Nightly Build <you@gmail.com>` |
| `MAIL_SMTP_SERVER` | `smtp.gmail.com` |
| `MAIL_SMTP_PORT` | `465` |
| `MAIL_SMTP_USERNAME` | `you@gmail.com` |
| `MAIL_SMTP_PASSWORD` | a Gmail App Password, or your provider's SMTP key |

Notes: without both the config block and `MAIL_TO`, the workflow gates itself
off silently. It skips mornings with no fresh build (rolling presses build
nightly; a completed press goes quiet). Test a send anytime by running the
workflow manually from the Actions tab (`workflow_dispatch` bypasses the hour
and freshness gates, not the secrets gate). Credentials live only in GitHub
Actions secrets — never in the repo, and never anywhere the editor's
untrusted-PR validation can see them.

Every night's digest is also archived at `builds/<date>/email.html` on the
site.

## catalog.json — the API

`https://<you>.github.io/<repo>/catalog.json` is the machine-readable state
of the whole library: series (with progress), every edition's nb-meta plus
`path`/`position`/`reading_minutes`, builds grouped by night, and the tag
index. The site's own search and contextual navigation run on it, and it is
a stable public contract — external readers, dashboards, or a future
multi-press directory can build on it without touching the repo.
