num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num)]

primary_diagonal = [matrix[i][i] for i in range(num)]
second_diagonal = [matrix[i][-1 - i] for i in range(num)]

print(abs(sum(primary_diagonal) - sum(second_diagonal)))