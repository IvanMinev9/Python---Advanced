# number = int(input())
# matrix = []

# for _ in range(number):
#     matrix.append([int(x) for x in input().split()])

# diagonal_sum = 0
# for row in range(number):
#     for col in range(number):
#         if row == col:
#             diagonal_sum += matrix[row][col]

# print(diagonal_sum)

number = int(input())

matrix = []

for _ in range(number):
    matrix.append([int(x) for x in input().split()])

diagonal_sum = 0

for row in range(number):
    for col in range(number):
        if row + col == number - 1:
            diagonal_sum += matrix[row][col]

print(diagonal_sum)