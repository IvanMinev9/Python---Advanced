rows, cols = [int(x) for x in input().split(', ')]
matrix = []
total = 0

for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)
    total += sum(data)

print(total)
print(matrix) 