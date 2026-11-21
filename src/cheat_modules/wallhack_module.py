from src.cheat_core.feature_handler import FeatureHandler
from src.cheat_core.pattern_scanner import PatternScanner, ScanTarget


class WallhackHandler(FeatureHandler):
    name = "wallhack"
    target = ScanTarget(name="wallhack_sig", signature="48 8B 05 ?? ?? ?? ?? 48 85 C0", module="engine.dll")

    def _enable(self) -> None:
        # writes depth-test bypass flag at resolved address
        pass

    def _disable(self) -> None:
        pass


def build_handler(scanner: PatternScanner) -> FeatureHandler:
    return WallhackHandler(scanner)