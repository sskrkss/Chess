from .figure import Figure

class Rook(Figure):
    def __str__(self):
        return 'R'

    def __repr__(self):
        return f'Rook({self.hor}, {self.ver})'

    def possible_moves(self):
        pos_hor_left = [(h, self.ver) for h in range(self.hor - 1, -1, -1)]
        pos_hor_right = [(h, self.ver) for h in range(self.hor + 1, 8)]
        pos_ver_up = [(self.hor, v) for v in range(self.ver - 1, -1, -1)]
        pos_ver_down = [(self.hor, v) for v in range(self.ver + 1, 8)]
        return [pos_hor_left, pos_hor_right, pos_ver_up, pos_ver_down]