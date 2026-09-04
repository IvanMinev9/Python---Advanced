def is_valid(row1, col1, row2, col2, rows, cols):
    return 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols

row, col = map(int, input().split())
matrix = [input().split() for _ in range(row)]

while True:
    line = input()
    if line == 'END':
        break

    command = line.split()

    if command[0] != 'swap' or len(command) != 5:
        print('Invalid input!')
        continue
    row1, col1, row2, col2 = map(int, command[1:])
    if is_valid(row1, col1, row2, col2, row, col):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print('Invalid input!')