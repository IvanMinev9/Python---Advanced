rows, cols = [int(x) for x in input().split(", ")]
matrix = []
submatrix = []

max_sum = float("-inf")
sum_of_submatrix = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row in range(rows - 1):
    for col in range(cols - 1):
        curr_element = matrix[row][col]
        next_element = matrix[row][col + 1]
        below_element = matrix[row + 1][col]
        diagonal_element = matrix[row + 1][col + 1]
        
        sum_of_submatrix = curr_element + next_element + below_element + diagonal_element
        if sum_of_submatrix > max_sum:
            max_sum = sum_of_submatrix
            submatrix = [
                [curr_element, next_element],
                [below_element, diagonal_element]
            ]

print(*submatrix[0])
print(*submatrix[1])
print(sum_of_submatrix)