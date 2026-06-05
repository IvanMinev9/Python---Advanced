size = int(input())

matrix = []

bunny_row = 0
bunny_col = 0

for row in range(size):

    current_row = input().split()
    matrix.append(current_row)

    if "B" in current_row:
        bunny_row = row
        bunny_col = current_row.index("B")


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

best_direction = ""
best_path = []
max_eggs = float("-inf")


for direction, (dr, dc) in directions.items():

    row = bunny_row + dr
    col = bunny_col + dc

    current_eggs = 0
    path = []

    while 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == "X":
            break

        current_eggs += int(matrix[row][col])
        path.append([row, col])

        row += dr
        col += dc

    if current_eggs > max_eggs and path:
        max_eggs = current_eggs
        best_direction = direction
        best_path = path


print(best_direction)

for position in best_path:
    print(position)

print(max_eggs)