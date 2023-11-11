from .piece import *


class Bishop(Piece):
    def __str__(self):
        return f'B({self.color})'

    def __repr__(self):
        return f'Bishop({self.hor}, {self.ver})'

    def moves_empty_board(self):
        up_right_direction = [(self.hor - s, self.ver + s) for s in range(1, 8 - max(7 - self.hor, self.ver))]
        up_left_direction = [(self.hor - s, self.ver - s) for s in range(1, min(self.hor, self.ver) + 1)]
        down_left_direction = [(self.hor + s, self.ver - s) for s in range(1, 8 - max(self.hor, 7 - self.ver))]
        down_right_direction = [(self.hor + s, self.ver + s) for s in range(1, 8 - max(self.hor, self.ver))]
        return [up_right_direction, up_left_direction, down_left_direction, down_right_direction]
