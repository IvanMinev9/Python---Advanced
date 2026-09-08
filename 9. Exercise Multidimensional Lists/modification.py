def is_valid(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def add(matrix, row, col, value):
    matrix[row][col] += value
    
def sub(matrix, row, col, value):
    matrix[row][col] -= value

rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break
    command = line.split()
    
    row, col, value = map(int, command[1:])
    
    if not is_valid(row, col, rows, len(matrix[0])):
        print("Invalid coordinates")
        continue
    
    if command[0] == "Add":
        add(matrix, row, col, value)
        
    if command[0] == "Subtract":
        sub(matrix, row, col, value)

[print(*row) for row in matrix]