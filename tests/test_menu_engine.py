from src.main.menu_engine import MenuEngine
from src.cheat_core.module_loader import ModuleLoader
from src.cheat_core.pattern_scanner import PatternScanner
from src.cheat_core.feature_handler import FeatureHandler


class _StubHandler(FeatureHandler):
    name = "stub"

    def _enable(self) -> None: ...

    def _disable(self) -> None: ...


def test_toggle_updates_state():
    scanner = PatternScanner()
    loader = ModuleLoader(scanner=scanner)

    class _Mod:
        name = "stub"
        @staticmethod
        def build_handler(_scanner):
            return _StubHandler(_scanner)

    loader.modules = [_Mod()]
    engine = MenuEngine(loader=loader, scanner=scanner)
    engine.hydrate()

    assert engine.snapshot_state() == {"stub": False}
    assert engine.toggle("stub") is True
    assert engine.snapshot_state()["stub"] is True
    assert engine.toggle("stub") is False
    assert engine.snapshot_state()["stub"] is False