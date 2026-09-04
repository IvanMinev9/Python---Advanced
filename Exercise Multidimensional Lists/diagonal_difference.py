number = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(number)]

prim_diagonal = [matrix[i][i] for i in range(number)]
second_diagonal = [matrix[i][-1 - i] for i in range(number)]

print(abs(sum(prim_diagonal) - sum(second_diagonal)))