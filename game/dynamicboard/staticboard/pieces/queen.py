from .piece import *


class Queen(Piece):
    def __str__(self):
        return f'Q({self.color})'

    def __repr__(self):
        return f'Queen({self.hor}, {self.ver})'

    def moves_empty_board(self):
        left_direction = [(self.hor, v) for v in range(self.ver - 1, -1, -1)]
        right_direction = [(self.hor, v) for v in range(self.ver + 1, 8)]
        up_direction = [(h, self.ver) for h in range(self.hor - 1, -1, -1)]
        down_direction = [(h, self.ver) for h in range(self.hor + 1, 8)]
        up_right_direction = [(self.hor - s, self.ver + s) for s in range(1, 8 - max(7 - self.hor, self.ver))]
        up_left_direction = [(self.hor - s, self.ver - s) for s in range(1, min(self.hor, self.ver) + 1)]
        down_left_direction = [(self.hor + s, self.ver - s) for s in range(1, 8 - max(self.hor, 7 - self.ver))]
        down_right_direction = [(self.hor + s, self.ver + s) for s in range(1, 8 - max(self.hor, self.ver))]
        return [
            left_direction, right_direction, up_direction, down_direction,
            up_right_direction, up_left_direction, down_left_direction, down_right_direction
        ]
