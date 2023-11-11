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
        self.last_move = None
        self.fifty_moves_counter = 0
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

    def is_piece(self, hor, ver):
        if self.board[hor][ver] is not EmptyCell:
            return True
        else:
            print('Вы выбрали пустую клетку. Попробуйте еще раз')

    def is_turn(self, hor, ver, turn):
        if self.board[hor][ver].color == turn:
            return True
        else:
            print('Вы выбрали чужую фигуру. Попробуйте еще раз')

    def possible_moves(self, hor, ver, color):
        selected_square = self.board[hor][ver]
        input_moves = selected_square.moves_empty_board()
        output_moves = []
        # bishop, queen, rook, knight, king
        if isinstance(selected_square, (Bishop, Queen, Rook, Knight, King)):
            for direction in input_moves:
                for h, v in direction:
                    target = self.board[h][v]
                    if target is EmptyCell:
                        output_moves.append((h, v))
                    else:
                        if color != target.color:
                            output_moves.append((h, v))
                        break
        # pawn
        elif selected_square is Pawn:
            updown_direction, diag_direction = input_moves
            # вертикальные ходы
            for h, v in updown_direction:
                target = self.board[h][v]
                if target is EmptyCell:
                    output_moves.append((h, v))
                else:
                    break
            # диагональные взятия
            for h, v in diag_direction:
                target = self.board[h][v]
                if isinstance(target, Piece) and color != target.color:
                    output_moves.append((h, v))
            # взятие на проходе
            for h, v in diag_direction:
                target = self.board[selected_square.hor][v]
                if (target is Pawn and color != target.color and
                        abs(selected_square.hor - target.previous_coord[0]) == 2 and
                        target == self.last_move):
                    output_moves.append((h, v))
        return output_moves

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

    def is_long_castling(self):
        #  в длинную сторону
        if (self.previous_coord == None and current_board[self.hor][0].previous_coord == None and
                all([type(current_board[self.hor][x]) == EmptyCell for x in range(1, 4)])):
            return self.hor, 2

    def is_short_castling(self):
        #  в короткую сторону
        if (self.previous_coord == None and current_board[self.hor][7].previous_coord == None and
                all([type(current_board[self.hor][x]) == EmptyCell for x in range(5, 6)])):
            return self.hor, 6

    def fifty_moves_rule(self):
        if isinstance(self.last_move, Pawn):
            self.fifty_moves_counter = 0
        else:
            self.fifty_moves_counter += 1