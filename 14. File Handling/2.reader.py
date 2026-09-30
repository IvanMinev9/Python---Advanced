from pathlib import Path

path = Path(__file__).parent.parent / "files" / "numbers.txt"

file = open(path)
numbers = [int(x) for x in file.read().split("\n") if x]
file.close()

print(sum(numbers))

# from pathlib import Path

# path = Path("files") / "numbers.txt"

# with open(path) as file:
#     numbers = [int(x) for x in file.read().split("\n") if x]

# print(sum(numbers)) automatic closes the file using "with"
