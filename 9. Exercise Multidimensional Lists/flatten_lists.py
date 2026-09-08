list_number = input().split("|")
matrix = []

for mat in reversed(list_number):
    if mat:
        numbers = mat.split()
        matrix.extend(numbers)

print(*matrix, sep=" ")