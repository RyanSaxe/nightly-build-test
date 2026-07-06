"""Put the engine on sys.path before the test scripts import it.

The suites are zero-framework scripts run directly from any working
directory, so `import check` and `import build_site` need engine/ on the
path before those import statements execute. Importing this module first
does that setup as an ordinary top-of-file import, which keeps every other
import at the top of the file where it belongs.
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "engine"))
