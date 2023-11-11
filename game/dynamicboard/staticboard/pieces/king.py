from .piece import *


class King(Piece):
    def __str__(self):
        return f'K({self.color})'

    def __repr__(self):
        return f'King({self.hor}, {self.ver})'

    def moves_empty_board(self):
        return [
            [(self.hor + i, self.ver + j)] for j in range(-1, 2) for i in range(-1, 2)
            if not j == i == 0 and 0 <= self.hor + i <= 7 and 0 <= self.ver + j <= 7
        ]
