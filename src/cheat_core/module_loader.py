import importlib
import logging
import pkgutil
from dataclasses import dataclass
from types import ModuleType
from typing import Callable, List

from src.cheat_core.pattern_scanner import PatternScanner

log = logging.getLogger(__name__)


@dataclass
class CheatModule:
    name: str
    package: str
    build_handler: Callable[[PatternScanner], "object"]


class ModuleLoader:
    """Discovers cheat module packages under a folder and exposes handlers."""

    def __init__(self, scanner: PatternScanner) -> None:
        self.scanner = scanner
        self.modules: List[CheatModule] = []

    def discover(self, path: str) -> List[CheatModule]:
        pkg = path.strip("./").replace("/", ".")
        try:
            root = importlib.import_module(pkg)
        except ImportError:
            log.warning("module root %s not importable", pkg)
            return self.modules

        for info in pkgutil.iter_modules(root.__path__):
            full = f"{pkg}.{info.name}"
            try:
                mod: ModuleType = importlib.import_module(full)
            except Exception as exc:  # noqa: BLE001
                log.error("failed to load module %s: %s", full, exc)
                continue
            builder = getattr(mod, "build_handler", None)
            if builder is None:
                continue
            self.modules.append(CheatModule(name=info.name, package=full, build_handler=builder))
        return self.modules