# AI agent file

import Gamestate as gs
from math import inf

class AI_agent:
    def __init__(self, board, player) -> None:
        self.Gamestates = []
        self.best_move = 0 # best move it can find
        self.board = board # current board
        self.player = player

    
    def search(self) -> int:
        """ searches for best move, returns best next move """

        # 1. need to create the first Gamestate
        initial_GS = gs.Gamestate(self.board, self.player, -1) # -1 as no move is picked yet

        # 2. need to perform first level of search
        evaluations = []
        for child in initial_GS.generate_children():
            evaluations.append((child.minimax(False), child.move))

        # 3. from list of children, return move that has highest value :)))
        self.best_move = max(evaluations)[1]