number = int(input())
matrix = []

for _ in range(number):
    data = [int(x) for x in input().split()]
    matrix.append(data)

sum = 0

for index in range(number):
    sum += matrix[index][index]

print(sum)