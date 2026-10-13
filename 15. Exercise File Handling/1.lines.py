from pathlib import Path

path = Path(__file__).parent.parent / "files" / "lines.txt"

with open(path) as f:
    for row, line in enumerate(f):
        if row % 2 == 0:
            for ch in {"-", ",", ".", "!", "?"}:
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))
