
size = int(input())

matrix = [input().split() for _ in range(size)]

# Намираме зайчето
bunny_row = 0
bunny_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_row = row
            bunny_col = col


# Функция, която проверява една посока
def check_direction(row, col, row_change, col_change):
    eggs = 0
    positions = []

    row += row_change
    col += col_change

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        eggs += int(matrix[row][col])
        positions.append([row, col])

        row += row_change
        col += col_change

    return eggs, positions


# Проверяваме четирите посоки

up_eggs, up_positions = check_direction(
    bunny_row, bunny_col, -1, 0
)

down_eggs, down_positions = check_direction(
    bunny_row, bunny_col, 1, 0
)

left_eggs, left_positions = check_direction(
    bunny_row, bunny_col, 0, -1
)

right_eggs, right_positions = check_direction(
    bunny_row, bunny_col, 0, 1
)


# Намираме най-добрата посока
directions = [
    ("up", up_eggs, up_positions),
    ("down", down_eggs, down_positions),
    ("left", left_eggs, left_positions),
    ("right", right_eggs, right_positions),
]

best_direction = directions[0]

for direction in directions:
    if direction[1] > best_direction[1]:
        best_direction = direction


print(best_direction[0])

for position in best_direction[2]:
    print(position)

print(best_direction[1])