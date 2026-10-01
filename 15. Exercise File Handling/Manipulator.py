import os

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
    
    elif command == "Rerplace":
        try:
            with open(file_name, "r+") as f:
                content = f.read()
                f.seek(0)
                f.truncate(0)
                f.write(content.replace(args[0], args[1]))
        except FileNotFoundError:
            print("An error occured")
    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")