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
        pass

    
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

    
    def generate_children(self):
        """ gnerate children of a given node """

        children = []
        board = []
        for i in range(len(self.board)):
            if ut.check_valid_move(i+1, self.board, debug=False):
                board = copy.deepcopy(self.board)
                board[i] = self.player
                child = Gamestate(board, self.other, i)
                children.append(child)
            board = []
        return children

        
    def minimax(self, maximising) -> int:
        """ minimax search agent, usues simply heuristic function and searches terminally. returns next best move """

        # check if node is terminal node (i.e. win state)
        if ut.check_winner(self.player, self.board) or ut.check_winner(self.other, self.board):
            print("win")
            return (-1) ** (not maximising)

        # check if no valid moves left
        if not (" " in self.board):
            print("draw")
            return 0
        
        
        for child in self.generate_children():
            if maximising:
                value = -inf
                value = max(value, child.minimax(False))
            else:
                value = inf    
                value = min(value, child.minimax(True))
        
        return value
    