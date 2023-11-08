from .piece import *


class Knight(Piece):
    def __str__(self):
        return f'N({self.color})'

    def __repr__(self):
        return f'Knight({self.hor}, {self.ver})'

    def moves_empty_board(self):
        return [
            (self.hor + i, self.ver + j) for j in range(-2, 3) for i in range(-2, 3)
            if 0 <= self.hor + i <= 7 and 0 <= self.ver + j <= 7 and abs(i) + abs(j) == 3
        ]

    def moves_current_board(self, current_board):
        input_moves = self.moves_empty_board()
        output_moves = []
        for hor, ver in input_moves:
            target = current_board[hor][ver]
            if type(target) == EmptyCell or (isinstance(target, Piece) and self.color != target.color):
                output_moves.append((hor, ver))
        return output_moves
