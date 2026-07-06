"""Resolve the active press root.

The rule: `press/` if it exists, else `press-example/`. Forks create press/
at setup (and never delete press-example/, which keeps their merges from
upstream clean); the upstream repo ships no press/ and dogfoods from
press-example/.
"""

import os


def press_root(repo):
    press = os.path.join(repo, "press")
    if os.path.isdir(press):
        return press
    return os.path.join(repo, "press-example")
