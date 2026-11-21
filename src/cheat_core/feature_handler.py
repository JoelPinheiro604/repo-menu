import logging
from abc import ABC, abstractmethod

from src.cheat_core.pattern_scanner import PatternScanner, ScanTarget

log = logging.getLogger(__name__)


class FeatureHandler(ABC):
    """Base class for every toggleable cheat inside the REPO Cheats Menu."""

    name: str = "unnamed"
    target: ScanTarget | None = None

    def __init__(self, scanner: PatternScanner) -> None:
        self.scanner = scanner
        self.active = False

    def activate(self) -> None:
        if self.active:
            return
        if self.target:
            addr = self.scanner.find(self.target)
            if addr is None:
                log.warning("%s: signature not found, skipping", self.name)
                return
        self._enable()
        self.active = True
        log.info("%s enabled", self.name)

    def deactivate(self) -> None:
        if not self.active:
            return
        self._disable()
        self.active = False

    @abstractmethod
    def _enable(self) -> None: ...

    @abstractmethod
    def _disable(self) -> None: ...