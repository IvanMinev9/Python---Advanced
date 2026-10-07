from pathlib import Path

path = Path(__file__).parent.parent / "files" 

files = {}

for element in path.iterdir():
    if element.is_file():
        ext = element.suffix
        files.setdefault(ext, []).append(element.name)
    
    elif element.is_dir():
        for file in element.iterdir():
            if file.is_file():
                ext = file.suffix
                files.setdefault(ext, []).append(file.name)

with open(path / "report.txt", "w") as output_file:
    for ext, file_names in sorted(files.items()):
        output_file.write(f"{ext}\n")
        for file_name in sorted(file_names):
            output_file.write(f"- - - {file_name}\n")