"""Build the C native helper used by the mem_reader for the REPO Cheats Menu."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src-native" / "mem_reader.c"
OUT = ROOT / "build" / "mem_reader.dll"


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    compiler = "cl.exe" if sys.platform == "win32" else "gcc"
    cmd = [compiler, "/LD" if compiler.endswith(".exe") else "-shared", str(SRC), f"/Fe{OUT}" if compiler.endswith(".exe") else f"-o{OUT}"]
    print("running:", " ".join(cmd))
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())