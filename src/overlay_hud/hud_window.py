import logging
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from src.main.menu_engine import MenuEngine

log = logging.getLogger(__name__)


class HudWindow(QWidget):
    """Transparent overlay that paints cheat status indicators over the target."""

    def __init__(self, engine: MenuEngine) -> None:
        super().__init__()
        self.engine = engine
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._rows: dict[str, QLabel] = {}

        layout = QVBoxLayout(self)
        for feature in engine.list_features():
            label = QLabel(f"[ ] {feature}", self)
            label.setStyleSheet("color:#7CFC9A; font-family:Consolas; font-size:11pt;")
            layout.addWidget(label)
            self._rows[feature] = label

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._refresh)
        self._timer.start(250)

    def _refresh(self) -> None:
        for feature, label in self._rows.items():
            active = self.engine.snapshot_state().get(feature, False)
            label.setText(f"[{'x' if active else ' '}] {feature}")