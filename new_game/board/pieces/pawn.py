from .figure import Figure

class Pawn(Figure):
    def __str__(self):
        return 'P'

    def __repr__(self):
        return f'Pawn({self.hor}, {self.ver})'

    def possible_moves(self):
        if self.color == 'w':
            if self.hor > 0:
                if self.hor == 6:
                    return [(self.hor - s, self.ver) for s in range(1, 3)]
                return [(self.hor - 1, self.ver)]
        if self.hor < 7:
            if self.hor == 1:
                return [(self.hor + s, self.ver) for s in range(1, 3)]
            return [(self.hor + 1, self.ver)]