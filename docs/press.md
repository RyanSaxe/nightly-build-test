# Your press — ownership, forks, and updates

## The one rule

**`press/` is yours. Everything else is the engine.**

Every file you will ever create or edit lives under `press/`: your series,
your voice, your title, your themes, your templates. Everything outside it —
`engine/`, `templates/`, `skills/`, `spec/`, `.github/`, `PROTOCOL.md` — is
upstream-owned machinery you never touch. This partition is not a convention
for tidiness; it is what makes the whole lifecycle conflict-free.

```
press/
  site.yaml          masthead title, theme, appearance, email delivery
  editorial.md       your voice — composed into every edition's instructions
  series/<id>/       series.yaml + prompt.md + sources/ per series
  series/_tags/      reusable prompt fragments shared across series
  themes/            custom design-token files
  templates/         your own edition templates (see docs/customization.md)
```

## The fork lifecycle

1. **Fork** with GitHub's "Copy the main branch only" box checked. You get
   the engine plus upstream's `press/` — which is the upstream project's own
   dogfood configuration, doubling as a living example.
2. **Set up**: say "set me up" to your agent. The Librarian resets `press/`
   to yours (series, voice, title) and runs `./setup.sh`, which creates the
   empty `library` branch, seeds its trigger workflows, and enables Pages +
   auto-merge. Enable workflows once in your fork's Actions tab.
3. **Publish forever**: the night shift adds editions to `library` via
   one-file PRs; `main` only changes when *you* change configuration or pull
   an engine update.

## Updating the engine (no merges, no conflicts)

Engine updates take upstream's version of every path outside `press/` and
never read or write `press/` itself:

```
git remote add upstream https://github.com/RyanSaxe/the-nightly-build.git   # once
git fetch upstream
git log upstream/main..HEAD --oneline -- . ':(exclude)press'    # must be empty
git checkout upstream/main -- . ':(exclude)press'
git commit -m "chore: sync engine from upstream"
./setup.sh    # re-syncs the trigger workflows onto library
```

If that `git log` prints anything, you (or an agent) edited engine-space;
move the change into `press/` before syncing, or it will be overwritten.
Your agent runs this whole procedure for you — ask it to "update my engine."

Because published editions live on the `library` branch and reference the
engine's assets by path, an engine update restyles and re-chromes your entire
back catalog on the next publish — permanence without staleness.

## Why upstream's press/ has content

The upstream repo runs its own configuration nightly (dogfooding), so its
Pages site is a live demo of exactly what a fork produces, and every config
file in its `press/` is a working example you can crib. Your fork replaces
that content at setup; the engine-update sync never brings it back.
