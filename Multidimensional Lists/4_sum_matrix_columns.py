rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for col in range(cols):
    coloum_sum = 0
    for row in range(rows):
        coloum_sum += matrix[row][col]
    print(coloum_sum)