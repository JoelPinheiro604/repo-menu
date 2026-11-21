import sys
import logging
from PySide6.QtWidgets import QApplication

from src.main.menu_engine import MenuEngine
from src.main.ipc.menu_bridge import MenuBridge
from src.shared.menu_contracts import APP_NAME, APP_VERSION
from src.cheat_core.module_loader import ModuleLoader
from src.cheat_core.pattern_scanner import PatternScanner
from src.overlay_hud.hud_window import HudWindow


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def main() -> int:
    configure_logging()
    log = logging.getLogger("repo-menu")
    log.info("starting %s v%s", APP_NAME, APP_VERSION)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)

    scanner = PatternScanner()
    loader = ModuleLoader(scanner=scanner)
    loader.discover("modules/")

    engine = MenuEngine(loader=loader, scanner=scanner)
    bridge = MenuBridge(engine=engine)
    bridge.attach()

    hud = HudWindow(engine=engine)
    hud.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())