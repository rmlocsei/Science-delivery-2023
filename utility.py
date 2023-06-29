
LEN_BOARD = 9
HUMAN = 0
RANDOM_AGENT = 1
AI_AGENT = 2
SYMBOL = 0
AGENT = 1

def print_board(board):
    print("-" * 13)
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-" * 13)
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-" * 13)
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-" * 13)

def make_move(player, board):
    """ makes move on board """
    while True:
        move = int(input("Player2: Enter a move between 1 and 9: "))
        if check_valid_move(move, board):
            board[move - 1] = player
            break


def check_valid_move(move, board, debug=True):
    """ checks if move is valid """
    valid = True
    if (move > LEN_BOARD) or (move < 1):
        if debug:
            print("Try a different move, this square is out of range!")
        valid = False
    if board[move - 1] != " ":
        if debug:
            print("This square is taken, try a different square!")
        valid = False
    return valid


def check_winner(player, board):
    """ checks if player has won game """
    WIN = True
    winning_combo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), \
                     (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]

    for combo in winning_combo:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return WIN
    return not WIN