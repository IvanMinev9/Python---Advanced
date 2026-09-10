def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size

def count_attacks(matrix, row, col, size):
    
    moves = [
        (-2, -1),
        (-2, 1),
        (2, -1),
        (2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2)
    ]
    
    attacks = 0
    
    for row_moves, col_moves in moves:
        new_row = row + row_moves
        new_col = col + col_moves
        
        if is_valid(new_row, new_col, size):
            if matrix[new_row][new_col] == "K":
                attacks += 1
    
    return attacks


size = int(input())
matrix = [list(input()) for _ in range(size)]
removed = 0

while True:
    max_attacks = 0
    max_row = -1
    max_col = -1
    
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attack = count_attacks(matrix, row, col, size)
                
                if attack > max_attacks:
                    max_attacks = attack
                    max_row = row
                    max_col = col
    
    if max_attacks == 0:
        break
    
    matrix[max_row][max_col] = "0"
    removed += 1
    
print(removed)
                


# ТЕКУЩ КОН
#    ↓
# (row, col)
#    ↓
#    + движение
#    ↓
# (new_row, new_col)
#    ↓
# валидна ли е позицията?
#    ↓
# има ли K там?
#    ↓
# ДА → attacks += 1