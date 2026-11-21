# Authoring a Cheat Module

A module is a single file in `src/cheat_modules/` that exports `build_handler(scanner)`.

## Minimum viable module

```python
from src.cheat_core.feature_handler import FeatureHandler
from src.cheat_core.pattern_scanner import PatternScanner, ScanTarget

class MyHandler(FeatureHandler):
    name = "my_cheat"
    target = ScanTarget(name="my_sig", signature="DE AD BE EF ?? ??", module="engine.dll")

    def _enable(self): ...
    def _disable(self): ...

def build_handler(scanner: PatternScanner) -> FeatureHandler:
    return MyHandler(scanner)
```

## Signature guidelines

- Wildcard every immediate that shifts between builds.
- Test against a known build; include the build hash in your PR.
- Never scan the whole process — restrict to the module in `ScanTarget.module`.

## Feature spec fields

Wallhack / ESP / aimbot handlers are expected to expose tunables as class attributes so the ControlsPanel can bind them later.