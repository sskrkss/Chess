from .figure import Figure

class Bishop(Figure):
    def __str__(self):
        return 'B'

    def __repr__(self):
        return f'Bishop({self.hor}, {self.ver})'

    def possible_moves(self):
        pos_up_right = [(self.hor - s, self.ver + s) for s in range(1, 8 - max(7 - self.hor, self.ver))]
        pos_up_left = [(self.hor - s, self.ver - s) for s in range(1, min(self.hor, self.ver) + 1)]
        pos_down_left = [(self.hor + s, self.ver - s) for s in range(1, 8 - max(self.hor, 7 - self.ver))]
        pos_down_right = [(self.hor + s, self.ver + s) for s in range(1, 8 - max(self.hor, self.ver))]
        return [pos_up_right, pos_up_left, pos_down_left, pos_down_right]