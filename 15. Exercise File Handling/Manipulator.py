# import os

# while True:
#     line = input()
#     if line == "End":
#         break
    
#     command, file_name, *args = line.split("-")
    
#     if command == "Create":
#         open(file_name, "w").close()
    
#     elif command == "Add":
#         with open(file_name, "a") as f:
#             f.write(args[0] + "\n")
    
#     elif command == "Rerplace":
#         try:
#             with open(file_name, "r+") as f:
#                 content = f.read()
#                 f.seek(0)
#                 f.truncate(0)
#                 f.write(content.replace(args[0], args[1]))
#         except FileNotFoundError:
#             print("An error occured")
#     elif command == "Delete":
#         if os.path.exists(file_name):
#             os.remove(file_name)
#         else:
#             print("An error occurred")


from pathlib import Path

BASE_PATH = Path(__file__).parent.parent / "files"

def create_file(file_path):
    file_path.write_text("")


def add_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content, "\n")
        
def replace_in_file(file_path, old_string, new_string):
    try:
        content = file_path.read_text()
        content = content.replace(old_string, new_string)
        file_path.write_text(content)
    except FileNotFoundError:
        print("An error occurred")

def delete_file(file_path):
    if file_path.exists():
        file_path.unlink()
    else:
        print("An error occurred")

commands = {
    "Create": create_file,
    "Add": add_to_file,
    "Replace": replace_in_file,
    "Delete": delete_file,
    
    }

while True: 
    line = input()
    if line == "End":
        break
    
    command, file_name, *args = line.split("-")
    
    file_path = BASE_PATH / file_name
    
    if command == "Create":
        commands[command](file_path)
    
    elif command == "Add":
        commands[command](file_path, args[0])
    
    elif command == "Replace":
        commands[command](file_path, args[0], args[1])
    
    elif command == "Delete":
        commands[command](file_path)