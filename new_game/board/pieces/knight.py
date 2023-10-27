from .figure import Figure

class Knight(Figure):
    def __str__(self):
        return 'N'

    def __repr__(self):
        return f'Knight({self.hor}, {self.ver})'