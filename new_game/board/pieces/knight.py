from .figure import Figure

class Knight(Figure):
    def __str__(self):
        return 'N'

    def __repr__(self):
        return f'Knight({self.hor}, {self.ver})'

    def possible_moves(self):
        return [
            (self.hor + i, self.ver + j) for j in range(-2, 3) for i in range(-2, 3)
            if 0 <= self.hor + i <= 7 and 0 <= self.ver + j <= 7 and abs(i) + abs(j) == 3
        ]