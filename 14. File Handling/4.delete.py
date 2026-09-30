from pathlib import Path

path = Path(__file__).parent.parent / "files" / "delete.txt"

path.unlink()
