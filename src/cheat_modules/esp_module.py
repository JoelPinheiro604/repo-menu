from src.cheat_core.feature_handler import FeatureHandler
from src.cheat_core.pattern_scanner import PatternScanner, ScanTarget


class EspHandler(FeatureHandler):
    name = "esp"
    target = ScanTarget(name="esp_sig", signature="E8 ?? ?? ?? ?? 8B 4D ?? 85 C9", module="engine.dll")

    draw_boxes = True
    draw_skeleton = True
    draw_health = True

    def _enable(self) -> None:
        pass

    def _disable(self) -> None:
        pass


def build_handler(scanner: PatternScanner) -> FeatureHandler:
    return EspHandler(scanner)