import logging
from typing import Callable, Dict, Any

from src.main.menu_engine import MenuEngine
from src.shared.menu_contracts import IPC_CHANNEL_TOGGLE, IPC_CHANNEL_LIST

log = logging.getLogger(__name__)


class MenuBridge:
    """Lightweight IPC bridge used by the renderer to talk to the engine."""

    def __init__(self, engine: MenuEngine) -> None:
        self.engine = engine
        self._listeners: Dict[str, Callable[..., Any]] = {}

    def attach(self) -> None:
        self._listeners[IPC_CHANNEL_LIST] = self._on_list
        self._listeners[IPC_CHANNEL_TOGGLE] = self._on_toggle
        self.engine.hydrate()
        log.info("menu bridge attached with %d channels", len(self._listeners))

    def dispatch(self, channel: str, payload: dict) -> Any:
        handler = self._listeners.get(channel)
        if handler is None:
            raise KeyError(f"no listener for channel {channel}")
        return handler(payload)

    def _on_list(self, _payload: dict) -> list[str]:
        return self.engine.list_features()

    def _on_toggle(self, payload: dict) -> dict:
        feature = payload["feature"]
        enabled = payload.get("enabled")
        return {"feature": feature, "enabled": self.engine.toggle(feature, enabled)}