import logging
from typing import Dict, List

from src.cheat_core.module_loader import ModuleLoader
from src.cheat_core.pattern_scanner import PatternScanner
from src.cheat_core.feature_handler import FeatureHandler
from src.shared.menu_contracts import MenuToggle, MODULE_STATE

log = logging.getLogger(__name__)


class MenuEngine:
    """Central dispatcher for all cheat toggles exposed by the REPO Cheats Menu."""

    def __init__(self, loader: ModuleLoader, scanner: PatternScanner) -> None:
        self.loader = loader
        self.scanner = scanner
        self._handlers: Dict[str, FeatureHandler] = {}
        self._state: Dict[str, bool] = {}

    def hydrate(self) -> None:
        for module in self.loader.modules:
            handler = module.build_handler(self.scanner)
            self._handlers[module.name] = handler
            self._state[module.name] = False
        log.info("hydrated %d cheat handlers", len(self._handlers))

    def list_features(self) -> List[str]:
        return sorted(self._handlers.keys())

    def toggle(self, feature: str, desired: bool | None = None) -> bool:
        handler = self._handlers.get(feature)
        if handler is None:
            raise KeyError(f"unknown cheat feature: {feature}")
        target = (not self._state[feature]) if desired is None else desired
        if target:
            handler.activate()
        else:
            handler.deactivate()
        self._state[feature] = target
        MODULE_STATE[feature] = target
        log.info("toggle %s -> %s", feature, target)
        return target

    def snapshot_state(self) -> Dict[str, bool]:
        return dict(self._state)

    def apply_toggle_batch(self, toggles: List[MenuToggle]) -> Dict[str, bool]:
        for t in toggles:
            self.toggle(t.feature, t.enabled)
        return self.snapshot_state()