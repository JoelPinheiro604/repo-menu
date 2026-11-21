from src.cheat_core.feature_handler import FeatureHandler
from src.cheat_core.pattern_scanner import PatternScanner, ScanTarget


class AimbotHandler(FeatureHandler):
    name = "aimbot"
    target = ScanTarget(name="aimbot_sig", signature="F3 0F 10 05 ?? ?? ?? ?? F3 0F 11", module="engine.dll")

    fov: float = 12.0
    smooth: float = 3.5
    bone: str = "head"

    def _enable(self) -> None:
        pass

    def _disable(self) -> None:
        pass


def build_handler(scanner: PatternScanner) -> FeatureHandler:
    return AimbotHandler(scanner)