from .piece import *


class King(Piece):
    def __str__(self):
        return f'K({self.color})'

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
            if type(target) == EmptyCell or (isinstance(target, Piece) and self.color != target.color):
                output_moves.append((hor, ver))
        return output_moves

    def long_castling(self, current_board):
        output_moves = []
        #  в длинную сторону
        if (self.previous_move == None and current_board[self.hor][0].previous_move == None and
                all([type(current_board[self.hor][x]) == EmptyCell for x in range(1, 4)])):
            output_moves.append((self.hor, 2))

    def short_castling(self, current_board):
        #  в короткую сторону
        if (self.previous_move == None and current_board[self.hor][7].previous_move == None and
                all([type(current_board[self.hor][x]) == EmptyCell for x in range(5, 6)])):
            return self.hor, 6
