matrix = []

player_row = 0
player_col = 0

targets = 0

for row in range(5):

    current_row = input().split()
    matrix.append(current_row)

    for col in range(5):

        if matrix[row][col] == "A":
            player_row = row
            player_col = col

        elif matrix[row][col] == "x":
            targets += 1


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

hit_targets = []

commands = int(input())

for _ in range(commands):

    command = input().split()

    action = command[0]
    direction = command[1]

    dr, dc = directions[direction]

    # MOVE
    if action == "move":

        steps = int(command[2])

        new_row = player_row + dr * steps
        new_col = player_col + dc * steps

        if 0 <= new_row < 5 and 0 <= new_col < 5:
            if matrix[new_row][new_col] == ".":

                matrix[player_row][player_col] = "."
                matrix[new_row][new_col] = "A"

                player_row = new_row
                player_col = new_col

    # SHOOT
    elif action == "shoot":

        shot_row = player_row + dr
        shot_col = player_col + dc

        while 0 <= shot_row < 5 and 0 <= shot_col < 5:

            if matrix[shot_row][shot_col] == "x":

                matrix[shot_row][shot_col] = "."
                hit_targets.append([shot_row, shot_col])

                targets -= 1
                break

            shot_row += dr
            shot_col += dc

    if targets == 0:
        print(f"Training completed! All {len(hit_targets)} targets hit.")
        break

else:
    print(f"Training not completed! {targets} targets left.")


for target in hit_targets:
    print(target)