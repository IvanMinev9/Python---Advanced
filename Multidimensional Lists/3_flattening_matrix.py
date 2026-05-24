num = int(input())
matrix = []

for _ in range(num):
    data = [int(x) for x in input().split(', ')]
    matrix.extend(data)

print(matrix)