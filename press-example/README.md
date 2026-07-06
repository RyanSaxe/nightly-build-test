# press-example/ — upstream's press, your reference

This is the upstream project's **own live configuration** — its night shift
researches these series nightly, which makes every file here a permanently
working example of the config surface (series modes, source policy, voice,
commented advanced options).

**In your fork, this folder is inert**: the engine reads `press/` when it
exists and only falls back to `press-example/` when it doesn't (that fallback
is how the upstream repo runs itself). Your setup scaffolds `press/`; this
folder just sits here as documentation.

Two rules keep your upstream merges clean:

1. **Don't edit anything in here** — put your configuration in `press/`.
2. **Don't delete this folder** — upstream keeps updating it, so deleting it
   would turn every future `git merge upstream/main` noisy for no benefit.

And one warning: if your repo has no `press/` at all, the engine falls back
to THIS folder — meaning a scheduled night shift would research upstream's
example syllabus instead of yours. Keep `press/` in place.
