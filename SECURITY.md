# Security Policy

## Supported versions

Only the `main` branch and the latest tagged release of REPO Cheats Menu receive fixes.

## Scope

Issues we care about:

- RCE reachable from a broken module signature
- Memory corruption in `src-native/mem_reader.c`
- Config injection through `%APPDATA%/repo-menu/*.json`
- Unauthorized elevation paths in `app_bootstrap.py`

## Out of scope

- Detection by any anti-cheat product — this is a known and expected risk
- Bans on game accounts — use at your own risk
- Signature drift after a game patch (that is a feature request, not a vuln)

## Reporting

Email `security@repo-menu.dev` with a PoC. Do not open public issues for exploits.