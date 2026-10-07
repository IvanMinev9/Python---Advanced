player_one = input("Player one name: ")
player_two = input("Player two name: ")
player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'").upper()

player_two = 'O' if player_one == 'X' else 'X'

print("This is the numeration of the board")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"{player_one} starts first")

def row_winner(matrix, sign):
    for row in matrix:
        if row.count(current_sign) == 3:
            return True
        return False

def col_winner(matrix, sign):
     for col_inx in range(3):
         count = 0
         for row_inx in range(3):
             if matrix[row_inx][col_inx] == sign:
                 count += 1
        
         if count == 3:
            return True
         return False

def diagonal_winner(matrix, sign):
    for index in range(3):
        if matrix[index][index] == sign:
            count += 1
        
    if count == 3:
        return True
    
    

def winner(matrix, sign):
    is_row_winner = row_winner(matrix, sign)
    
def print_matrix(board):
    for row in matrix:
        print(f"| {' | '.join(row)} |")
     
matrix = [[" ", " ", " "] for _ in range(3)]
mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0), 
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

turns = 1

while True:
    current_player = player_one if turns % 2 != 0 else player_two
    current_sign = player_one if turns % 2 != 0 else player_two
    
    try:
        position = int(input(f"{current_player} please choose a free position between [1-9]"))
    
    except ValueError:
        print("Please a valid position")
        continue
    
    if not (1 <= position <= 9):
        print("Please enter valid number, between 1 and 9")
        continue
    
    row, col = mapper(position)
    if matrix[row][col] != " ":
        print("Possition taken")
        continue
    matrix[row][col] = current_sign
    
    if turns >= 5:
        winner(matrix)
    turns += 1
    print(matrix)