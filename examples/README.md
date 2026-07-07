# examples/: a complete, working press

A full press configuration, kept as living documentation. Six desks show the
whole surface:

- `frontier-compute/` is a **collection** of company dossiers (article,
  Dossier form) with per-item prompts, `consult` sources, and shared tag
  fragments.
- `ai-history/` is a **sequence** of chronicles (article, Chronicle form),
  each building on the last.
- `transformers-101/` is a **sequence** course (article, Lesson form).
- `landmark-papers/` is a **collection** of appraisals (article, Appraisal
  form).
- `daily-brief/` is a **rolling** nightly brief, slugged by date.
- `wildcard/` is an **open desk** that picks its own topic and form each night.

Between them they exercise both templates, the form system (a free-text label
plus the shared furniture in `templates/FURNITURE.md`), the source policy
(`consult` live, `required_docs` and `sources_exclusive` shown as documented
options), rhythm controls (`cadence`, `paused`, `selection`), word-band and
source-floor calibration, tag fragments, a voice file, and commented advanced
options in every series.yaml.

The engine never reads this folder. To use any of it, copy files into your
`press/` and edit:

```
cp -r examples/series/ai-history press/series/my-history
```

The upstream repo is engine-only; it runs no press of its own. The maintainer
dogfoods by forking this repo like any other user.
