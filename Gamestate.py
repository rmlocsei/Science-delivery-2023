# Gamestate class for AI agent

from math import inf
import utility as ut
import copy 

class Gamestate:
    winning_combo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), \
                     (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
    
    def __init__(self, board, player, move) -> None:
        self.board = board # current board
        self.player = player # the player's symbol
        self.move = move
    
    def __str__(self) -> str:
        return f"board is {self.board}, player symbol is {self.player}, move to get to it is {self.move}"

    
    
    def get_symbol(self):
        return self.player
        
    def other_player(self):
        """ get opponent's symbol """
        if self.player == "0":
            opponent = "x"
        else:
            opponent = "0"
        return opponent

    
    def generate_children(self, player):
        """ generate children of a given node """

        children = []
        board = []
        for i in range(len(self.board)):
            if ut.check_valid_move(i+1, self.board, debug=False):
                board = copy.deepcopy(self.board)
                board[i] = player
                child = Gamestate(board, player, i)
                children.append(child)
            board = []
        return children

        
    def minimax(self, player, maximising) -> int:
        """ minimax search agent, usues simply heuristic function and searches terminally. returns next best move """

        # check if node is terminal node (i.e. win state)
        if ut.check_winner(self.player, self.board):
            if maximising:
                return -1
            else:
                return 1

        # check if no valid moves left
        if not (" " in self.board):
            return 0
        
        if maximising:
            value = -inf
        else:
            value = inf
        for child in self.generate_children(player):
            if maximising:
                value = max(value, child.minimax(child.other_player(), False))
            else:    
                value = min(value, child.minimax(child.other_player(), True))
        
        return value
    