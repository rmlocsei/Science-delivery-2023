# Gamestate class for AI agent

import main
from math import inf

class Gamestate:
    winning_combo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), \
                     (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
    
    def __init__(self, path, board, player, move) -> None:
        self.path = path # list of moves (integers) to get from initial gamestate to terminal gamestate
        self.board = board # current board
        self.player = player # the player's symbol
        self.move = move
        self.eval = 0 # evaluation of node (how good it is)
    
    def heuristic(self) -> int:
        """ calculates how good a state is by counting the number of possible wins for that state """
        
        possible_wins = 0
        
        # get opponent's symbol
        opponent = self.other

        board = self.board
        
        # get all possible wins
        piece_locs = [(board[combo[0]], board[combo[1], board[combo[2]]]) for combo in self.winning_combo]
        for pieces in piece_locs:
            if not (opponent in pieces):
                possible_wins += 1
        
        return possible_wins
    
        
    def other(self):
        """ get opponent's symbol """
        if self.player == "0":
            opponent = "X"
        else:
            opponent = "0"
        return opponent
    
    """def setup(self, parent, move, board):
        """ """setup value of child node from parent node info""" """
        self.path = parent.path + [move]
        self.board = board
        self.player = parent.other
        self.eval = self.heuristic"""

    
    def generate_children(self):
        """ gnerate children of a given node """

        children = []
        for i in range(len(self.board)):
            if main.check_valid_move(i, self.board):
                board = self.board
                board[i] = self.player
                child = Gamestate(self.path + [i], board, self.other)
                child.eval = child.heuristic()
                children.append(child)

        return children

        
    def minimax(self, maximising) -> int:
        """ minimax search agent, usues simply heuristic function and searches terminally. returns next best move """

        # check if node is terminal node (i.e. win state)
        if main.check_winner(self.player, self.board):
            return self.eval
        # check if no valid moves left
        if " " not in self.board:
            return 
        
        
        for child in self.generate_children:
            if maximising:
                value = -inf
                value = max(value, child.minimax(False))
            else:
                value = inf    
                value = min(value, child.minimax(True))
        
        return value
    