size_board = int(input())

board = [list(input()) for _ in range(size_board)]

moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

removed_knights = 0

def is_valid(rows, cols):
    return 0 <= rows < size_board and 0 <= cols < size_board

while True:
    max_attacks = 0
    knights_row = 0
    knights_col = 0

    for row in range(size_board):
        for col in range(size_board):

            if board[row][col] == 'K':

                attacks = 0

                for dr, dc in moves:
                    new_row = row + dr
                    new_col = col + dc

                    if is_valid(new_row, new_col):
                        if board[new_row][new_col] == 'K':
                            attacks += 1
                
                if attacks > max_attacks:
                    max_attacks = attacks
                    knights_row = row
                    knights_col = col
    
    if max_attacks == 0:
        break

    board[knights_row][knights_col] = '0'
    removed_knights += 1

print(removed_knights)