from .cell_and_piece import *

class King(Piece):
    def __str__(self):
        return 'K'

    def __repr__(self):
        return f'King({self.hor}, {self.ver})'

    def moves_empty_board(self):
        return [
            (self.hor + i, self.ver + j) for j in range(-1, 2) for i in range(-1, 2)
            if not j == i == 0 and 0 <= self.hor + i <= 7 and 0 <= self.ver + j <= 7
        ]
    def moves_current_board(self, current_board):
        input_moves = self.moves_empty_board()
        output_moves = []
        for hor, ver in input_moves:
            target = current_board[hor][ver]
            if type(target) == EmptyCell or (isinstance(target, Figure) and self.color != target.color):
                output_moves.append((hor, ver))
        return output_moves