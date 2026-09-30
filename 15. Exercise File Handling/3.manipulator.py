# from pathlib import Path

# path = Path(__file__).parent.parent / "files" / ""
while True:
    line = input()
    if line == "End":
        break

    command, file_name, *args = line.split("-")

    if command == "Create":
        open(file_name, "w").close()
    elif command == "Add":
        with open(file_name, "a") as f:
            f.write(args[0] + "\n")
    elif command == "Replace":
        try:
            with open(file_name, "r+") as f:
                content = f.read()
                f.seek(0)
                f.truncate()
                f.write(content.reaplace(args[0], args[1]))
        except FileNotFoundError:
            print("An error occurred")
    elif command == "Delete":
        pass
