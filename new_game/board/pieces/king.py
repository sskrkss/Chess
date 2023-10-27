from .figure import Figure

class King(Figure):
    def __str__(self):
        return 'K'

    def __repr__(self):
        return f'King({self.hor}, {self.ver})'

    def possible_moves(self):
        return [
            (self.hor + i, self.ver + j) for j in range(-1, 2) for i in range(-1, 2)
            if not j == i == 0 and 0 <= self.hor + i <= 7 and 0 <= self.ver + j <= 7
        ]