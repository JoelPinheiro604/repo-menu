"""Dev helper: drop a new cheat module into src/cheat_modules from a template."""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "src" / "cheat_modules"

TEMPLATE = '''from src.cheat_core.feature_handler import FeatureHandler
from src.cheat_core.pattern_scanner import PatternScanner, ScanTarget


class {cls}(FeatureHandler):
    name = "{name}"
    target = ScanTarget(name="{name}_sig", signature="", module="engine.dll")

    def _enable(self) -> None:
        pass

    def _disable(self) -> None:
        pass


def build_handler(scanner: PatternScanner) -> FeatureHandler:
    return {cls}(scanner)
'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    args = ap.parse_args()
    slug = re.sub(r"[^a-z0-9_]", "_", args.name.lower())
    cls = "".join(p.capitalize() for p in slug.split("_")) + "Handler"
    path = MODULES / f"{slug}_module.py"
    path.write_text(TEMPLATE.format(cls=cls, name=slug), encoding="utf-8")
    print(f"created {path}")


if __name__ == "__main__":
    main()