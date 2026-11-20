"""Write this entry's news image to the grader's output directory.

The finished image lives in the repository as entry.png, next to this file.
This program's only job is to place an exact copy of it at
<output>/entry.png, where <output> is /output when the grader runs it and
$MAKEFUN_OUTPUT_DIR for a local run. A plain byte copy means every run
writes identical bytes.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry image not found: {SOURCE}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    if _sha256(target) != _sha256(SOURCE):
        raise RuntimeError("copied image does not match the source byte for byte")


if __name__ == "__main__":
    main()
