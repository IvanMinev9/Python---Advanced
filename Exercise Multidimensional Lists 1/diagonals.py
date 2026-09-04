num = int(input())
matrix = [[int(x) for x in input().split(", ")] for i in range(num)]

primary_diagonal = [matrix[i][i] for i in range(num)]
second_diagonal = [matrix[i][-1 - i] for i in range(num)]

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}')

print(matrix)