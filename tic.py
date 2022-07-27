print('Welcome to the amazing game of Tic Tac Toe!l')

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def nice_board(board):
    for a in board:
        print(a)


def check_board(grid):
    tie_check = 0
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != '-':
            nice_board(board)
            print(f'The winner is {row[0]}')
            return False
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[2][2] != '-':
        nice_board(board)
        print(f'The winner is {grid[0][0]}')
        return False
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[2][0] != '-':
        nice_board(board)
        print(f'The winner is {grid[1][1]}')
        return False
    if grid[0][0] == grid[1][0] == grid[2][0] and grid[2][0] != '-':
        nice_board(board)
        print(f'The winner is {grid[0][0]}')
        return False
    if grid[0][1] == grid[1][1] == grid[2][1] and grid[2][1] != '-':
        nice_board(board)
        print(f'The winner is {grid[0][1]}')
        return False
    if grid[0][2] == grid[1][2] == grid[2][2] and grid[2][2] != '-':
        nice_board(board)
        print(f'The winner is {grid[0][2]}')
        return False

    for row in grid:
        if '-' not in row:
            tie_check += 1
    if tie_check == 3:
        nice_board(board)
        print('The game ended in a tie')
        return False
    else:
        return True


def X_turn(board):
    nice_board(board)
    row = get_row()
    column = get_column()
    if board[row][column] != '-':
        print('That spot is taken!')
        return X_turn(board)
    else:
        board[row][column] = 'X'


def O_turn(board):
    nice_board(board)
    row = get_row()
    column = get_column()
    if board[row][column] != '-':
        print('That spot is taken!')
        return O_turn(board)
    else:
        board[row][column] = 'O'


def get_row():
    if turn_count % 2 == 0:
        row = input(f'In which row would you like to place an X? (1 - Top, 2 - Middle, 3 - Bottom) ')
    else:
        row = input(f'In which row would you like to place an O? (1 - Top, 2 - Middle, 3 - Bottom) ')
    if row.isdecimal() == False or row == '':
        print('Invalid input. Only 1, 2 or 3 please')
        return get_row()
    elif 1 > int(row) or 3 < int(row):
        print('Invalid input. Only 1, 2 or 3 please')
        return get_row()
    else:
        row = int(row) - 1
        return row


def get_column():
    if turn_count % 2 == 0:
        column = input(f'In which column would you like to place an X? (1 - Top, 2 - Middle, 3 - Bottom) ')
    else:
        column = input(f'In which column would you like to place an O? (1 - Top, 2 - Middle, 3 - Bottom) ')
    if column.isdecimal() == False or column == '':
        print('Invalid input. Only 1, 2 or 3 please')
        return get_column()
    elif 1 > int(column) or 3 < int(column):
        print('Invalid input. Only 1, 2 or 3 please')
        return get_column()
    else:
        column = int(column) - 1
        return column


turn_count = 0
while check_board(board) == True:
    if turn_count % 2 == 0:
        print('~' * 50)
        print('Player X, it\'s your turn! ')
        check_board(board)
        X_turn(board)
        turn_count += 1

    else:
        print('~' * 50)
        print('Player O, it\'s your turn! ')
        check_board(board)
        O_turn(board)
        turn_count += 1


