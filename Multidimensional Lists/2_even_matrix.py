number = int(input())
matrix = []

for _ in range(number):
    data = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(data)

print(matrix)