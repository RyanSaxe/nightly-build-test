# Customization: look, voice, and your own templates

Everything here happens inside `press/` (see [press.md](press.md)). Engine
updates never touch it. Working examples live in `examples/`.

## Look: themes

The entire visual system reads about 14 CSS variables from one token file.
The theme contract: define exactly those variables, in all four blocks
(light, dark, and the two manual-override blocks). The test suite enforces
parity across the blocks.

The shipped theme pairs a pale day-sky paper with bronze accents in light
mode and a deep navy night with amber in dark mode. Keep day accents deep
if you customize: contrast is measured, and bronze #8A5C08 reads at 5.4:1
on the shipped paper while bright amber fails at 2:1.

1. Copy `engine/assets/themes/newspaper.css` to `press/themes/<name>.css`.
2. Edit the variables in all four blocks.
3. Point `press/site.yaml` at it: `theme: press/themes/<name>.css`.

The builder republishes the chosen theme as `assets/theme.css` on every
publish, so a theme change restyles the whole library, every past edition
included. Base tokens are light, the universal fallback; dark applies via
`prefers-color-scheme` or the reader's toggle. Keep it that way in custom
themes.

Fonts load from Google Fonts, the only allowed external origin besides the
engine's own assets. Swapping families changes the chrome and new editions
immediately; editions published earlier keep their frozen font links and
fall back to system faces for any family they did not load.

## Voice: press/editorial.md

Your paper's voice, composed into every edition's instructions after the
house style (`spec/editorial.md`) and before any series prompt. Register,
language, assumed background, banned habits: anything that should hold
across every series. Series-specific emphasis belongs in that series'
`prompt.md`. Per-topic angles belong in tag fragments
(`press/series/_tags/`).

The layer order, first to last. Later layers specialize and never override:

```
PROTOCOL.md > spec/editorial.md > press/editorial.md > template registry
entry > press/series/<id>/prompt.md > tag fragments > item prompt
```

## Your own templates

User templates are first class: the proof enforces whatever a registry
entry declares, so a template you invent gets the same validation, CI, and
site treatment as the shipped five.

1. Declare it in `press/templates/registry.yaml`:

```yaml
fieldnotes:
  class: shortread
  words: [800, 2000]
  sections: [observations, open-questions, sources]
  cite_rule: per-section
  modes: [rolling, collection]
```

Rules: `sections` must include `sources` and lists the required minimum
(editions may add extra sections). Bands are `[low, high]`. `cite_rule` is
`per-section`, `per-item` (needs `data-nb-item` markers), or `per-slide`
(needs `data-nb-slide`). Entries here overlay the shipped registry, so
reusing a shipped id redefines it.

2. Scaffold it as `press/templates/fieldnotes.html`. Copy a shipped
template's `<head>` and header chrome verbatim (asset links, nb-meta
skeleton, eyebrow, title, dek, byline), then lay out one
`<section data-nb-section="...">` per declared section. Template files
shadow shipped ones by filename. The sandbox applies unchanged: no scripts
beyond the JSON blocks and the engine runtime, citations as `sup.nb-cite`
anchors into numbered source entries.

3. Validate and rehearse: `python3 engine/validate_config.py`, then point a
series at the template and run a press check before scheduling it.

## site.yaml reference

```yaml
title: "My Press"                # masthead; the accent period is added
theme: press/themes/mytheme.css  # default: the shipped newspaper theme
appearance: auto                 # auto | light | dark
front: compact                   # compact (default) | comfortable (deks on story cells)
email:                           # optional, see docs/delivery.md
  send_utc_hour: 12
```
