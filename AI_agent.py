# AI agent file

import Gamestate as gs
from math import inf
import copy

class AI_agent:
    
    winning_combo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), \
                     (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
    
    def __init__(self, board, player) -> None:
        self.Gamestates = []
        self.board = board # current board
        self.player = player

    
    def search(self) -> int:
        """ searches for best move, returns best next move """

        # 1. need to create the first Gamestate
        initial_GS = gs.Gamestate(self.board, self.player, -1) # -1 as no move is picked yet

        # 2. need to perform first level of search
        evaluations = []
        
        for child in initial_GS.generate_children(self.player):
            # print(child)
            # print(child.move)
            evaluations.append((child.minimax(initial_GS.other_player(), False), child.move))
        # print(evaluations)
        best = max(evaluations)[1]
        return best
    
    def heuristic(self) -> int:
        """ calculates how good a state is by counting the number of possible wins for that state """
        
        possible_wins = 0
        
        # get opponent's symbol
        opponent = self.other()

        board = self.board
        
        # get all possible wins
        piece_locs = [(board[combo[0]], board[combo[1]], board[combo[2]]) for combo in self.winning_combo]
        # print("pieve_locs", piece_locs)
        for pieces in piece_locs:
            if not (opponent in pieces) and self.player in pieces:
                possible_wins += 1
        
        return possible_wins
    
    def other(self):
        """ get opponent's symbol """
        if self.player == "0":
            opponent = "x"
        else:
            opponent = "0"
        return opponent