from .empty_cell import EmptyCell
from .figure import Figure

class Pawn(Figure):
    def __str__(self):
        return 'P'

    def __repr__(self):
        return f'Pawn({self.hor}, {self.ver})'

    def moves_empty_board(self):  # без учета превращения пешки
        if self.color == 'w':  # ветка для белой пешки

            #  вертикальные ходы
            if self.hor == 6:  # первый ход
                updown_direction = [(self.hor - s, self.ver) for s in range(1, 3)]
            else:  # остальные ходы
                updown_direction = [(self.hor - 1, self.ver)]

            #  диагональные взятия
            if self.ver == 0 or self.ver == 7: # крайние пешки
                diag_direction = [(self.hor - 1, self.ver - 1), (self.hor - 1, self.ver + 1)][self.ver == 0]
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

        return updown_direction, diag_direction

    def moves_current_board(self, current_board):
        updown_direction, diag_direction = self.moves_empty_board()
        output_moves = []

        #  вертикальные ходы
        for hor, ver in updown_direction:
            target = current_board[hor][ver]
            if type(target) == EmptyCell:
                output_moves.append((hor, ver))
            else:
                break

        #  диагональные взятия
        for hor, ver in updown_direction:
            target = current_board[hor][ver]
            if isinstance(target, Figure) and self.color != target.color:
                output_moves.append((hor, ver))

        return output_moves