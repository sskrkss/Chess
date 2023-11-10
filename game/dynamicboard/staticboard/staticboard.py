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
        self.w_king_coord = 7, 4
        self.b_king_coord = 0, 4
        self.king_coord = {'w': self.w_king_coord, 'b': self.b_king_coord}

    def __str__(self):
        return '\n'.join(' '.join(str(c).center(4) for c in h) for h in self.board)

    def __repr__(self):
        return '\n'.join(' '.join(repr(c).ljust(15) for c in h) for h in self.board)

    def show_coord(self):
        return '\n'.join(' '.join(c.coord for c in h) for h in self.board)

    def show_square(self):
        return '\n'.join(' '.join(c.square for c in h) for h in self.board)

    def find_king(self, color):
            h, v = self.king_coord[color]
            return self.board[h][v]

    def possible_moves(self, hor, ver, color):
        selected_square = self.board[hor][ver]
        if isinstance(selected_square, Piece):
            if selected_square.color == color:
                input_moves = selected_square.moves_empty_board()
                output_moves = []
                # завтра продолжим
                for h, v in input_moves:
                    target = self.board[h][v]
                    if target is EmptyCell or (isinstance(target, Piece) and color != target.color):
                        output_moves.append((hor, ver))
                return output_moves
            else:
                print('Вы выбрали чужую фигуру. Попробуйте еще раз')
        else:
            print('Вы выбрали пустую клетку. Попробуйте еще раз')

    def is_check(self, color):
        h, v = self.king_coord[color]
        input_moves = Queen(h, v, color).moves_empty_board()
        for direction in input_moves:
            for hor, ver in direction:
                target = self.board[hor][ver]
                if isinstance(target, Piece) and color == target.color:
                    break
                elif isinstance(target, Piece) and color != target.color:
                    return True

    def is_checkmate(self, color):
        if self.is_check(color) and not self.moves_current_board() and not self.is_defence():
            return True

    def is_stalemate(self, current_board):
        if (not self.is_check(current_board) and not self.moves_current_board(current_board) and
                not self.any_moves(current_board)):
            return True

