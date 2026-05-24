rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

max_sum = float('-inf')
sub_matrix = []

for index_row in range(rows - 1):
    for index_col in range(cols - 1):
        current = matrix[index_row][index_col]
        next_element = matrix[index_row][index_col + 1]
        below_element = matrix[index_row + 1][index_col]
        diagonal_element = matrix[index_row + 1][index_col + 1]

        sum_elements = current + next_element + below_element + diagonal_element
        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [
                [current, next_element],
                [below_element, diagonal_element]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)