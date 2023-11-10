from .piece import *


class Knight(Piece):
    def __str__(self):
        return f'N({self.color})'

    def __repr__(self):
        return f'Knight({self.hor}, {self.ver})'

    def moves_empty_board(self):
        return [
            (self.hor + i, self.ver + j) for j in range(-2, 3) for i in range(-2, 3)
            if 0 <= self.hor + i <= 7 and 0 <= self.ver + j <= 7 and abs(i) + abs(j) == 3
        ]
