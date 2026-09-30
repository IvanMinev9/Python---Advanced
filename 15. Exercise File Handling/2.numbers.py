from pathlib import Path
from string import punctuation

path = Path(__file__).parent.parent / "files" / "line_numbers.txt"
output_path = Path(__file__).parent.parent / "files" / "output.txt"
result = []

with open(path) as input_file, open(output_path, "w") as output_file:
    for row, line in enumerate(input_file):
        letters_count = sum(ch.isalpha() for ch in line)
        punc_count = sum(ch in punctuation for ch in line)

        result.append(f"Line: {row + 1} {line.strip()} ({letters_count})({punc_count})")

    output_file.write("\n".join(result))
