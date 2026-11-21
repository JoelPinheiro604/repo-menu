from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QCheckBox

from src.shared.menu_contracts import MenuConfig


class ConfigPanel(QWidget):
    """Config editor for REPO Cheats Menu runtime settings."""

    def __init__(self, config: MenuConfig) -> None:
        super().__init__()
        self.config = config
        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.process_field = QLineEdit(config.process_name, self)
        self.hotkey_field = QLineEdit(config.hotkey_toggle, self)
        self.auto_attach = QCheckBox(self)
        self.auto_attach.setChecked(config.auto_attach)

        form.addRow("Target process", self.process_field)
        form.addRow("Hotkey toggle", self.hotkey_field)
        form.addRow("Auto attach", self.auto_attach)
        layout.addLayout(form)

    def collect(self) -> MenuConfig:
        return MenuConfig(
            auto_attach=self.auto_attach.isChecked(),
            process_name=self.process_field.text().strip() or "game.exe",
            hotkey_toggle=self.hotkey_field.text().strip() or "INSERT",
            show_overlay=self.config.show_overlay,
        )