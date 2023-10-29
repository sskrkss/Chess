from .board import *

class NewGame(ChessBoard):
    def move(self, h1, v1, h2, v2):
        if (h2, v2) in self.select(h1, v1):
            self.board[h2][v2] = self.board[h1][v1]
            self.board[h1][v1] = EmptyCell(h1, v1)
        else:
            print('Такого хода нет')