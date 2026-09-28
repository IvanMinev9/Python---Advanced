from pathlib import Path

path = Path(__file__).parent.parent / "files" / "text.txt"

try: 
    file = open(path)
    print("file found")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file not found")
