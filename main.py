# naughts and crosses by Rose-Maree Locsei 2023 for Science Delivery

LEN_BOARD = 9
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
            print_board(board)
            break


def check_valid_move(move, board):
    """ checks if move is valid """
    valid = True
    if (move > LEN_BOARD) or (move < 1):
        print("Try a different move, this square is out of range!")
        valid = False
    if board[move - 1] != " ":
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

def initiate_game():
    """ begin game """
    player1 = input("Enter the symbol you wish to play as (0 or X): ")
    if player1 == "0":
        player2 = "x"
    else:
        player2 = "0"
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    return (player1, player2, board)

player1, player2, board = initiate_game()

num_turns = 0
move = 0
game_over = False
while True:
    if num_turns >= 9:
        print("No one wins :(")
        break

    # player2's turn
    if num_turns % 2:
        player = player2
    else:
        player = player1
    
    make_move(player, board)
    if check_winner(player, board):
        print(player + " wins!")
        break
    
    num_turns += 1




