import logging
import re
from dataclasses import dataclass
from typing import Iterable, Optional

log = logging.getLogger(__name__)


@dataclass
class ScanTarget:
    name: str
    signature: str
    module: str


class PatternScanner:
    """Signature scanner used to locate hook points inside target processes."""

    def __init__(self, process: Optional[str] = None) -> None:
        self.process = process
        self._cache: dict[str, int] = {}

    def attach(self, process: str) -> None:
        self.process = process
        self._cache.clear()
        log.info("attached scanner to process %s", process)

    def find(self, target: ScanTarget) -> Optional[int]:
        if target.name in self._cache:
            return self._cache[target.name]
        if self.process is None:
            return None
        addr = self._simulate_scan(target.signature)
        if addr is not None:
            self._cache[target.name] = addr
        return addr

    def _simulate_scan(self, signature: str) -> Optional[int]:
        # real implementation walks module pages; here we validate signature form
        if not re.fullmatch(r"[0-9A-Fa-f ?]{4,}", signature):
            return None
        return 0x140000000 + (hash(signature) & 0xFFFFF)

    def resolve_all(self, targets: Iterable[ScanTarget]) -> dict[str, Optional[int]]:
        return {t.name: self.find(t) for t in targets}