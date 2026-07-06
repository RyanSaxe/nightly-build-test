#!/usr/bin/env python3
"""Generate valid fixture editions used by the test suite."""
import pathlib

FIX = pathlib.Path(__file__).parent / "fixtures"
FIX.mkdir(parents=True, exist_ok=True)

LOREM = ("The memory industry operates on a brutal capacity cycle that has bankrupted "
         "dozens of firms over four decades, and understanding that cycle is the "
         "precondition for judging any single company inside it. ")


def dossier():
    sec_defs = [
        ("orientation", "Orientation", 3),
        ("foundations", "Memory economics 101", 8),
        ("analysis", "Micron's position", 8),
        ("debate", "Bull versus bear", 6),
        ("go-deeper", "Go deeper", 3),
    ]
    ci = 0
    body = []
    for sid, title, paras in sec_defs:
        ps = []
        for _ in range(paras):
            n = (ci % 8) + 1
            ci += 1
            ps.append(f'<p>{LOREM * 6}'
                      f'<sup class="nb-cite"><a href="#s{n}">{n}</a></sup></p>')
        body.append(f'<section data-nb-section="{sid}">'
                    f'<h2>{title}</h2>{"".join(ps)}</section>')

    src = []
    for i in range(1, 9):
        req = ' data-nb-required="mu-10k-2025"' if i == 1 else ""
        href = ("https://www.sec.gov/filings/mu-10k" if i == 2
                else f"https://example.org/src{i}")
        src.append(f'<li id="s{i}"><span>Source {i}</span> '
                   f'<a data-nb-source{req} href="{href}">link</a></li>')

    meta = """{
  "protocol": "1.0", "series": "semiconductors", "slug": "micron",
  "template": "dossier", "title": "Micron Technology: The Scarcest Commodity in AI",
  "mode": "collection", "order": null, "date": "2026-07-06", "tags": ["equity"],
  "sources": 8, "words": 5400, "reading_minutes": 15,
  "dek": "How a cyclical commodity maker became the AI era's bottleneck.",
  "harness": "test-fixture", "model": "claude-fable-5"
}"""
    chart = ('{"type":"bar","labels":["FY23","FY24","FY25"],'
             '"series":[{"name":"Revenue $B","values":[15.5,25.1,37.4]}]}')

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Micron Technology</title>
<link href="https://fonts.googleapis.com/css2?family=Newsreader&amp;display=swap" rel="stylesheet">
<script type="application/json" id="nb-meta">
{meta}
</script>
<style>body{{font-family:serif}}</style>
</head><body>
<article>
{"".join(body)}
<figure>
<script type="application/json" data-nb-chart>
{chart}
</script>
</figure>
<section data-nb-section="sources"><h2>Sources</h2><ol>{"".join(src)}</ol></section>
</article>
</body></html>"""


def brief(date="2026-07-06"):
    items = []
    for i in range(1, 6):
        items.append(
            f'<div data-nb-item><span class="tag">topic{i}</span>'
            f'<h4>Development number {i} happened today'
            f'<sup class="nb-cite"><a href="#s{i}">{i}</a></sup></h4>'
            f'<p>Two sentences of what happened and the immediate context around it. '
            f'The specifics are grounded in the cited source.</p>'
            f'<p data-nb-why><b>Why it matters</b> — it moves the larger story we track.</p>'
            f'</div>')
    src = "".join(
        f'<li id="s{i}"><a data-nb-source href="https://example.org/news{i}">src</a></li>'
        for i in range(1, 6))
    meta = f"""{{
  "protocol": "1.0", "series": "ai-briefs", "slug": "{date}",
  "template": "brief", "title": "Daily brief for {date}",
  "mode": "rolling", "order": null, "date": "{date}", "tags": [],
  "sources": 5, "words": 300, "reading_minutes": 5,
  "dek": "Five items, each with why it matters.",
  "harness": "test-fixture", "model": "claude-fable-5"
}}"""
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Brief {date}</title>
<script type="application/json" id="nb-meta">
{meta}
</script>
</head><body>
<section data-nb-section="items">{"".join(items)}</section>
<section data-nb-section="sources"><ol>{src}</ol></section>
</body></html>"""


if __name__ == "__main__":
    (FIX / "valid-dossier.html").write_text(dossier())
    (FIX / "valid-brief.html").write_text(brief())
    print("fixtures written:", sorted(p.name for p in FIX.iterdir()))
