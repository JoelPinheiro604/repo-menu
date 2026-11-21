# Contributing to REPO Cheats Menu

Thanks for wanting to help out. This is a hobbyist modding project targeting the REPO engine — please keep PRs focused on the cheat menu itself.

## Ground rules

- Every new cheat module lives in `src/cheat_modules/` and exposes `build_handler(scanner)`.
- Signatures must be versioned against the game build you tested on — include the build hash in your PR description.
- UI work goes in `src/renderer/`. Do not touch `src/main/ipc/` without a maintainer review.
- Native helpers in `src-native/` are C, compiled by `scripts/build_native.py`. Keep them small.

## Local dev

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.main.app_bootstrap
```

## Adding a cheat

```bash
python scripts/inject_module.py aim_snap
```

Then fill in the signature and enable/disable logic. Do not commit empty modules.

## Reporting broken signatures

Open an issue tagged `signature-outdated` with the game build number and what module broke.