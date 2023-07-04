from random import choice
import AI_agent as ai


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

def make_move(player, board, debug=True):
    """ makes move on board """
    if player[AGENT] == HUMAN:
        while True:
            move = int(input("Player: Enter a move between 1 and 9: "))
            if check_valid_move(move, board, debug=True):
                board[move - 1] = player[SYMBOL]
                break
    elif player[AGENT] == RANDOM_AGENT:
        options = [i for i in range(len(board)) if board[i] == " "]
        move = choice(options)
        board[move] = player[SYMBOL]
    else:
        agent = ai.AI_agent(board, player[SYMBOL])
        best_move = agent.search()
        board[best_move] = player[SYMBOL]
        


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
        idx1, idx2, idx3 = combo[0], combo[1], combo[2]
        if (board[idx1] == board[idx2]) and (board[idx2] == board[idx3]) and  (board[idx3] == player):
            return WIN
    return not WIN