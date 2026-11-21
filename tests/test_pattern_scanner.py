from src.cheat_core.pattern_scanner import PatternScanner, ScanTarget


def test_scan_returns_none_when_unattached():
    scanner = PatternScanner()
    target = ScanTarget(name="aimbot_sig", signature="F3 0F 10 05 ?? ?? ?? ??", module="engine.dll")
    assert scanner.find(target) is None


def test_scan_resolves_signature_when_attached():
    scanner = PatternScanner()
    scanner.attach("game.exe")
    target = ScanTarget(name="wallhack_sig", signature="48 8B 05 ?? ?? ?? ??", module="engine.dll")
    addr = scanner.find(target)
    assert addr is not None and addr > 0
    assert scanner.find(target) == addr