# naughts and crosses by Rose-Maree Locsei 2023 for Science Delivery

import AI_agent as ai
import Gamestate as gs
import utility as ut


LEN_BOARD = 9
HUMAN = 0
RANDOM_AGENT = 1
AI_AGENT = 2
SYMBOL = 0
AGENT = 1

def initiate_game():
    """ begin game """

    player1, player2 = [0,0], [0,0]
    player1[SYMBOL] = input("Player1: Enter the symbol you wish to play as (0 or x): ")
    player1[AGENT] = int(input("Player1: Who do you wish to play as? Enter 0 for human, 1 for random agent, or 2 for AI agent. "))
    player2[AGENT] = int(input("Player2: Who do you wish to play as? Enter 0 for human, 1 for random agent, or 2 for AI agent. "))
    if player1[SYMBOL] == "0":
        player2[SYMBOL] = "x"
    else:
        player2[SYMBOL] = "0"
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # now we play
    play(player1, player2, board)
    return 
    
def play(player1, player2, board):
    """ if user chooses to play another human, then we play using this simple function """
    ut.print_board(board)
    num_turns = 0
    while True:
        if num_turns >= 9:
            print("No one wins :(")
            break

        # player2's turn
        if num_turns % 2:
            player = player2
        else:
            player = player1
    
        ut.make_move(player, board)

        ut.print_board(board)

        if ut.check_winner(player[SYMBOL], board):
            print(player[SYMBOL] + " wins!")
            break
    
        num_turns += 1  

initiate_game()










