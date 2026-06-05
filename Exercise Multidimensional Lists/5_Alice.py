size = int(input())

matrix = []
alice_row = 0
alice_col = 0

for row in range(size):

    current_row = input().split()
    matrix.append(current_row)

    if "A" in current_row:
        alice_row = row
        alice_col = current_row.index("A")


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea_bags = 0

matrix[alice_row][alice_col] = "*"

while tea_bags < 10:

    command = input()

    dr, dc = directions[command]

    new_row = alice_row + dr
    new_col = alice_col + dc

    # извън матрицата
    if not (0 <= new_row < size and 0 <= new_col < size):
        print("Alice didn't make it to the tea party.")
        break

    cell = matrix[new_row][new_col]

    # rabbit hole
    if cell == "R":
        matrix[new_row][new_col] = "*"
        print("Alice didn't make it to the tea party.")
        break

    # tea bags
    if cell.isdigit():
        tea_bags += int(cell)

    matrix[new_row][new_col] = "*"

    alice_row = new_row
    alice_col = new_col

else:
    print("She did it! She went to the party.")


for row in matrix:
    print(*row)