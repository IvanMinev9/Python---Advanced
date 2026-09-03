presents = int(input())
size = int(input())

matrix = []

santa_row = 0
santa_col = 0

nice_kids = 0
happy_kids = 0

for row in range(size):

    current_row = input().split()
    matrix.append(current_row)

    for col in range(size):

        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col

        elif matrix[row][col] == "V":
            nice_kids += 1


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


while presents > 0:

    command = input()

    if command == "Christmas morning":
        break

    dr, dc = directions[command]

    new_row = santa_row + dr
    new_col = santa_col + dc

    matrix[santa_row][santa_col] = "-"

    santa_row = new_row
    santa_col = new_col

    cell = matrix[santa_row][santa_col]

    # NICE KID
    if cell == "V":
        presents -= 1
        happy_kids += 1

    # COOKIE
    elif cell == "C":

        for move_row, move_col in directions.values():

            around_row = santa_row + move_row
            around_col = santa_col + move_col

            if matrix[around_row][around_col] in ["V", "X"]:

                if matrix[around_row][around_col] == "V":
                    happy_kids += 1

                presents -= 1
                matrix[around_row][around_col] = "-"

                if presents == 0:
                    break

    matrix[santa_row][santa_col] = "S"

    if presents == 0:
        break


if presents == 0 and happy_kids < nice_kids:
    print("Santa ran out of presents!")


for row in matrix:
    print(*row)


if happy_kids == nice_kids:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - happy_kids} nice kid/s.")