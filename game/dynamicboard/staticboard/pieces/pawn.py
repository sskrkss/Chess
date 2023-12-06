from .piece import *


class Pawn(Piece):
    def __str__(self):
        return f'P({self.color})'

    def __repr__(self):
        return f'Pawn({self.hor}, {self.ver})'

    def moves_empty_board(self):
        if self.color == 'w':  # ветка для белой пешки

            #  вертикальные ходы
            if self.hor == 6:  # первый ход
                updown_direction = [(self.hor - s, self.ver) for s in range(1, 3)]
            else:  # остальные ходы
                updown_direction = [(self.hor - 1, self.ver)]

            #  диагональные взятия
            if self.ver == 0 or self.ver == 7: # крайние пешки
                diag_direction = [((self.hor - 1, self.ver - 1), (self.hor - 1, self.ver + 1))[self.ver == 0]]
            else:  # срединные пешки:
                diag_direction = [(self.hor - 1, self.ver - 1), (self.hor - 1, self.ver + 1)]

        elif self.color == 'b':  # ветка для черной пешки

            #  вертикальные ходы
            if self.hor == 1:  # первый ход
                updown_direction = [(self.hor + s, self.ver) for s in range(1, 3)]
            else:  # остальные ходы
                updown_direction = [(self.hor + 1, self.ver)]

            #  диагональные взятия
            if self.ver == 0 or self.ver == 7:  # крайние пешки
                diag_direction = [((self.hor + 1, self.ver - 1), (self.hor + 1, self.ver + 1))[self.ver == 0]]
            else:  # срединные пешки:
                diag_direction = [(self.hor + 1, self.ver - 1), (self.hor + 1, self.ver + 1)]
        else:
            return

        return updown_direction, diag_direction
