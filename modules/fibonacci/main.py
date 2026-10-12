from modules.fibonacci.core import 
command = input()
sec = None

while command != "Stop":
    if command.startswith("Create"):
        num = int(command.split()[-1])
        sec = 