number = int(input())
matrix = []
position = None

for _ in range(number):
    data = list(input())
    matrix.append(data)

symbol = input()

for row in range(number):
    for col in range(number):
        if matrix[row][col] == symbol:
            position = (row, col)
            print(position)
            exit()
print(f"{symbol} does not occur in the matrix")