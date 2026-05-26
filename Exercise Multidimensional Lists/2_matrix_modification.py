matrix_rows = int(input())
matrix = []

for _ in range(matrix_rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command == 'END':
        break

    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if 0 <= row < matrix_rows and 0 <= col < len(matrix[row]):
        
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for rows in matrix:
    print(*rows)