from .pieces import *


class StaticBoard:
    _row1 = [
        Rook(0, 0, 'b'), Knight(0, 1, 'b'), Bishop(0, 2, 'b'), Queen(0, 3, 'b'),
        King(0, 4, 'b'), Bishop(0, 5, 'b'), Knight(0, 6, 'b'), Rook(0, 7, 'b')
    ]
    _row2 = [Pawn(1, v, 'b') for v in range(8)]
    _row3 = [EmptyCell(2, v) for v in range(8)]
    _row4 = [EmptyCell(3, v) for v in range(8)]
    _row5 = [EmptyCell(4, v) for v in range(8)]
    _row6 = [EmptyCell(5, v) for v in range(8)]
    _row7 = [Pawn(6, v, 'w') for v in range(8)]
    _row8 = [
        Rook(7, 0, 'w'), Knight(7, 1, 'w'), Bishop(7, 2, 'w'), Queen(7, 3, 'w'),
        King(7, 4, 'w'), Bishop(7, 5, 'w'), Knight(7, 6, 'w'), Rook(7, 7, 'w')
    ]
    _start_board = [_row1, _row2, _row3, _row4, _row5, _row6, _row7, _row8]

    def __init__(self):
        self.board = self._start_board
        self.fifty_moves_counter = 0
        self.last_move = None
        self.b_king_coord = 0, 4
        self.w_king_coord = 7, 4

    def __str__(self):
        return '\n'.join(' '.join(str(c).center(4) for c in h) for h in self.board)

    def __repr__(self):
        return '\n'.join(' '.join(repr(c).ljust(15) for c in h) for h in self.board)

    def show_coord(self):
        return '\n'.join(' '.join(c.coord for c in h) for h in self.board)

    def show_square(self):
        return '\n'.join(' '.join(c.square for c in h) for h in self.board)

    def find_king(self, turn):
        if turn == 'w':
            h, v = self.w_king_coord
            return self.board[h][v]
        elif turn == 'b':
            h, v = self.b_king_coord
            return self.board[h][v]
