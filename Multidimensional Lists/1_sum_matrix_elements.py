n_rows, n_colums = (int(x) for x in input().split(", "))

matrix = []

for _ in range(n_rows):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)

print(sum(data))
print(matrix)