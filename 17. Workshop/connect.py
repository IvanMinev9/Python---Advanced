class InvalidColumnError(Exception):
    pass

class TakenPossitionError(Exception):
    pass
    
def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    for line in matrix:
        print(line)

def validate_column_choise(col, max_cols):
    if not 0 <= col < max_cols:
        raise InvalidColumnError

def place_player_choice(matrix, c, player_num):
    for r in range(len(matrix) -1, -1, -1):
        if matrix[r][c] == 0:
            matrix[r][c] = player_num
            return r, c
    raise TakenPossitionError

def is_player_num(matrix, r, c, player_num):
    if r < 0 or c < 0 or r >= len(matrix) or col >= len(matrix[0]):
        return False
    return matrix[r][c] == player_num

def is_vertical_win(matrix, r, c, player_num, slots):
    return all(is_player_num(matrix, r+ idx, c, player_num) for idx in range(slots))
    
def is_horizontal_win(matrix, r, c, player_num, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(matrix, r, c + idx, player_num):
            filled += 1
        else:
            break
    
    for idx in range(1, slots):
        if is_player_num(matrix, r, c - idx, player_num):
            filled += 1
        else:
            break
        
    return filled >= slots

def right_diag_win(matrix, r, c, player_num, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(matrix, r - idx, c + idx, player_num):
            filled += 1
        else:
            break
    
    for idx in range(1, slots):
        if is_player_num(matrix, r + idx, c - idx, player_num):
            filled += 1
        else:
            break
        
    return filled >= slots

def left_diag_win(matrix, r, c, player_num, slots):
    filled = 1
    
    for idx in range(1, slots):
        if is_player_num(matrix, r - idx, c - idx, player_num):
            filled += 1
        else:
            break
    
    for idx in range(1, slots):
        if is_player_num(matrix, r + idx, c + idx, player_num):
            filled += 1
        else:
            break
        
    return filled >= slots
        
def is_winner(matrix, r, c, player_num, slots):
    return any([
        is_vertical_win(matrix, r, c, player_num, slots),
        is_horizontal_win(matrix, r, c, player_num, slots),
        left_diag_win(matrix, r, c, player_num, slots),
        right_diag_win(matrix, r, c, player_num, slots)
    ])

rows = 6
cols = 7
matrix = create_matrix(rows, cols)
print_matrix(matrix)

player = 1
counter = 0

while True:
    try:
        colum_num = int(input(f"Player {player}, please choose a column: ")) - 1
        validate_column_choise(colum_num, cols - 1)
        row, col = place_player_choice(matrix, colum_num, player)
        print_matrix(matrix)
        
        if is_winner(matrix, row, col, player):
            print(f"The winner is Player {player}")
            break
        
        counter += 1
        if rows * cols == counter:
            print("The game is draw!")
            break
        player = 2 if player == 1 else 1
    
    
    except TakenPossitionError:
        print("This column is already taken, please select another!")
        continue
    
    except InvalidColumnError:
        print(f"Please, select column between [1 - {cols}]!")
        continue
        
    except ValueError as err: 
        print(f"Please, enter a valid number - more information -> {err}")
        continue
    