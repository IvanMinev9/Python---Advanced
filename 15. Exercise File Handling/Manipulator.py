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
        commands[command](file_name)