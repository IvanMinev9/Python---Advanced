number = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(number)]

prim_diagonal = [matrix[i][i] for i in range(number)]
second_diagonal = [matrix[i][-1 - i] for i in range(number)]

print(f"Primary diagonal: {', '.join(map(str, prim_diagonal))}. Sum: {sum(prim_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")