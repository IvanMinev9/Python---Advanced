rows, cols = map(int, input().split())
snake = input()

index = 0

for row in range(rows):
    current_row = ""

    for col in range(cols):
        current_row += snake[index % len(snake)]
        index += 1

    if row % 2 == 0:
        print(current_row)
    else:
        print(current_row[::-1])