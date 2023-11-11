from .piece import *


class Rook(Piece):
    def __str__(self):
        return f'R({self.color})'

    def __repr__(self):
        return f'Rook({self.hor}, {self.ver})'

    def moves_empty_board(self):
        left_direction = [(self.hor, v) for v in range(self.ver - 1, -1, -1)]
        right_direction = [(self.hor, v) for v in range(self.ver + 1, 8)]
        up_direction = [(h, self.ver) for h in range(self.hor - 1, -1, -1)]
        down_direction = [(h, self.ver) for h in range(self.hor + 1, 8)]
        return [left_direction, right_direction, up_direction, down_direction]
