from dataclasses import dataclass, field
from typing import Dict


@dataclass
class HotkeyBinding:
    feature: str
    key: str
    modifiers: tuple[str, ...] = field(default_factory=tuple)


DEFAULT_BINDINGS: Dict[str, HotkeyBinding] = {
    "wallhack": HotkeyBinding("wallhack", "VK_F1"),
    "esp": HotkeyBinding("esp", "VK_F2"),
    "aimbot": HotkeyBinding("aimbot", "VK_F3"),
    "menu": HotkeyBinding("menu", "VK_INSERT"),
}


def parse_bindings(raw: dict) -> Dict[str, HotkeyBinding]:
    out: Dict[str, HotkeyBinding] = {}
    for feature, spec in raw.items():
        out[feature] = HotkeyBinding(
            feature=feature,
            key=spec["key"],
            modifiers=tuple(spec.get("modifiers", [])),
        )
    return out