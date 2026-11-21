import logging
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLabel

from src.main.ipc.menu_bridge import MenuBridge
from src.shared.menu_contracts import IPC_CHANNEL_TOGGLE

log = logging.getLogger(__name__)


class ControlsPanel(QWidget):
    """Sidebar with the toggle checkboxes for every cheat module."""

    def __init__(self, bridge: MenuBridge) -> None:
        super().__init__()
        self.bridge = bridge
        self.setWindowTitle("REPO Cheats Menu")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Modules"))

        for feature in bridge.dispatch("menu:list", {}):
            box = QCheckBox(feature, self)
            box.stateChanged.connect(lambda state, f=feature: self._on_toggle(f, state))
            layout.addWidget(box)

    def _on_toggle(self, feature: str, state: int) -> None:
        result = self.bridge.dispatch(
            IPC_CHANNEL_TOGGLE, {"feature": feature, "enabled": bool(state)}
        )
        log.info("panel toggle result: %s", result)