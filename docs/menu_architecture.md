# REPO Cheats Menu — Architecture

The menu is a layered desktop utility. Four rings, from boot to cheat:

1. **Bootstrap** — `src/main/app_bootstrap.py` wires the Qt app, the engine, the IPC bridge, and the HUD overlay.
2. **Engine** — `src/main/menu_engine.py` dispatches toggles to feature handlers loaded by `ModuleLoader`.
3. **Feature handlers** — every cheat under `src/cheat_modules/` subclasses `FeatureHandler` and declares a `ScanTarget`.
4. **Overlay** — `src/overlay_hud/hud_window.py` paints live toggle state on top of the game.

The native helper in `src-native/mem_reader.c` handles the raw `ReadProcessMemory` calls because ctypes overhead was unacceptable at 240 Hz.

## Data flow

```
[ControlsPanel] --toggle--> [MenuBridge] --dispatch--> [MenuEngine] --activate--> [FeatureHandler]
                                                              |
                                                              v
                                                        [PatternScanner]
                                                              |
                                                              v
                                                       [mem_reader.dll]
```

## Threading

All cheat handlers run on the Qt main thread. Signature scans are done once at enable time and cached in `PatternScanner._cache`.