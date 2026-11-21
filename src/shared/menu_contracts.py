from dataclasses import dataclass
from typing import Dict

APP_NAME = "REPO Cheats Menu"
APP_VERSION = "2026.02"
CONFIG_DIR = "%APPDATA%/repo-menu"

IPC_CHANNEL_LIST = "menu:list"
IPC_CHANNEL_TOGGLE = "menu:toggle"
IPC_CHANNEL_CONFIG = "menu:config"

MODULE_STATE: Dict[str, bool] = {}


@dataclass
class MenuToggle:
    feature: str
    enabled: bool


@dataclass
class MenuConfig:
    auto_attach: bool = True
    process_name: str = "game.exe"
    hotkey_toggle: str = "INSERT"
    show_overlay: bool = True