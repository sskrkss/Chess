from .board import *

class NewGame(ChessBoard):
    def select(self, hor, ver):
        selected_cell = self.board[hor][ver]
        print(selected_cell)
        if isinstance(selected_cell, Figure):
            print(selected_cell.moves_current_board(self.board))