from .figure import Figure

class Queen(Figure):
    def __str__(self):
        return 'Q'

    def __repr__(self):
        return f'Queen({self.hor}, {self.ver})'

    def possible_moves(self):
        pos_hor_left = [(h, self.ver) for h in range(self.hor - 1, -1, -1)]
        pos_hor_right = [(h, self.ver) for h in range(self.hor + 1, 8)]
        pos_ver_up = [(self.hor, v) for v in range(self.ver - 1, -1, -1)]
        pos_ver_down = [(self.hor, v) for v in range(self.ver + 1, 8)]
        pos_up_right = [(self.hor - s, self.ver + s) for s in range(1, 8 - max(7 - self.hor, self.ver))]
        pos_up_left = [(self.hor - s, self.ver - s) for s in range(1, min(self.hor, self.ver) + 1)]
        pos_down_left = [(self.hor + s, self.ver - s) for s in range(1, 8 - max(self.hor, 7 - self.ver))]
        pos_down_right = [(self.hor + s, self.ver + s) for s in range(1, 8 - max(self.hor, self.ver))]
        return [
            pos_hor_left, pos_hor_right, pos_ver_up, pos_ver_down,
            pos_up_right, pos_up_left, pos_down_left, pos_down_right
        ]