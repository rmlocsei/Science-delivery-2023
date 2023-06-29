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

    player1, player2 = (0,0), (0,0)
    opponent = input("Who do you wish to play? Enter 0 for human, 1 for random agent, or 2 for AI agent.")
    player1[SYMBOL] = int(input("Player1: Enter the symbol you wish to play as (0 or X): "))
    player1[AGENT] = int(input("Player1: Who do you wish to play as? Enter 0 for human, 1 for random agent, or 2 for AI agent."))
    player2[AGENT] = int(input("Player2: Who do you wish to play as? Enter 0 for human, 1 for random agent, or 2 for AI agent."))
    if player1[SYMBOL] == "0":
        player2[SYMBOL] = "x"
    else:
        player2[SYMBOL] = "0"
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # now we play
    if opponent == HUMAN:
        return 
    elif opponent == RANDOM_AGENT:
        return
    elif opponent == AI_AGENT:
        return
    return 
    
def play_human(player1, player2, board):
    """ if user chooses to play another human, then we play using this simple function """

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
    
        make_move(player, board)
        if check_winner(player, board):
            print(player + " wins!")
            break
    
        num_turns += 1  

def play_random(player1, player2, board):
    """ if user chooses to play random agent, then we just need to chooses 
            to randomly place pieces from available ones """
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
    
        make_move(player, board)
        if check_winner(player, board):
            print(player + " wins!")
            break
    
        num_turns += 1  

# player1, player2, board, opponent = initiate_game()
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
play = ai.AI_agent(board, "0")
play.search()
print(play.best_move)










