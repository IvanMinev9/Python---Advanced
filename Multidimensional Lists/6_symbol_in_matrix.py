number = int(input())
matrix = []

for _ in range(number):
    data = list(input())
    matrix.append(data)

symbol = input()
position = None

for index_row in range(number):
    for index_col in range(number):
        if matrix[index_row][index_col] == symbol:
            position = (index_row, index_col)
            print(position) 
            exit()
