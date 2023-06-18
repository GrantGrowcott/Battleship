board = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
next_player = {'X': 'O', 'O': 'X'}
current_player = 'X'


def display_board(board):
    """Prints out the game board in a nice format"""
    row1 = '|'.join(board[0])
    row2 = '|'.join(board[1])
    row3 = '|'.join(board[2])
    print('\n-----\n'.join((row1, row2, row3)))


def ask_for_move(board):
    """Asks user for move, returns it once validated"""
    print(f"It is {current_player}'s turn")
    valid_move = False
    while not valid_move:
        move = input('Please select a move (a-i): ')
        for row in board:
            for square in row:
                if square == move:
                    valid_move = True
    return move


def update_board(board, move):
    """Return a board with another X or O on it"""
    for row_index, row in enumerate(board):
        for square_index, square in enumerate(row):
            if square == move:
                board[row_index][square_index] = current_player


def equal_squares(squares):
    return squares[0] == squares[1] == squares[2]


def winning_position(board):
    """Check if there is a winning position on the board"""
    for row in board:
        if equal_squares(row):
            return True
    for column in zip(*board):
        if equal_squares(column):
            return True
    # Diagonals
    if equal_squares([board[0][0], board[1][1], board[2][2]]):
        return True
    if equal_squares([board[0][2], board[1][1], board[2][0]]):
        return True


def full_board(board):
    for row in board:
        for square in row:
            if square not in ['X', 'O']:
                return False
    return True


while not winning_position(board) and not full_board(board):
    display_board(board)
    move = ask_for_move(board)
    update_board(board, move)
    current_player = next_player[current_player]
    print('-'*30)


display_board(board)
if winning_position(board):
    print(f'The winner is {next_player[current_player]}!')
else:
    print('It is a tie!')

# HINT: You probably want to check for a tie as well
