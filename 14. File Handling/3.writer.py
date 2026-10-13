from pathlib import Path

path = Path(__file__).parent.parent / "files" / "my_first_file.txt"
with open(path, "w") as file:
    file.write("I just created my first file!")
