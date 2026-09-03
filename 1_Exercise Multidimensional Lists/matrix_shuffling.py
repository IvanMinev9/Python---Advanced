def is_valid(row1, col1, row2, col2, rows, cols):
    return 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols

rows, cols = map(int, input().split())
matrix = [input().split()]

while True:
    data = input()
    if data == "END":
        break
     
    command = data.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue
    r1, c1, r2, c2 = map(int, command[1:])
    
    if is_valid(r1, c1, r2, c2, rows, cols):
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")