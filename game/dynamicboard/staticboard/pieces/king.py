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

    def moves_current_board(self, current_board):  # с учетом блокировки от шаха
        input_moves = self.moves_empty_board()
        output_moves = []
        for hor, ver in input_moves:
            target = current_board[hor][ver]
            if type(target) == EmptyCell or (isinstance(target, Piece) and self.color != target.color):
                output_moves.append((hor, ver))
        return output_moves

    def long_castling(self, current_board):
        #  в длинную сторону
        if (self.previous_coord == None and current_board[self.hor][0].previous_coord == None and
                all([type(current_board[self.hor][x]) == EmptyCell for x in range(1, 4)])):
            return self.hor, 2

    def short_castling(self, current_board):
        #  в короткую сторону
        if (self.previous_coord == None and current_board[self.hor][7].previous_coord == None and
                all([type(current_board[self.hor][x]) == EmptyCell for x in range(5, 6)])):
            return self.hor, 6

    def is_check(self, current_board):
        left_direction = [(self.hor, v) for v in range(self.ver - 1, -1, -1)]
        right_direction = [(self.hor, v) for v in range(self.ver + 1, 8)]
        up_direction = [(h, self.ver) for h in range(self.hor - 1, -1, -1)]
        down_direction = [(h, self.ver) for h in range(self.hor + 1, 8)]
        up_right_direction = [(self.hor - s, self.ver + s) for s in range(1, 8 - max(7 - self.hor, self.ver))]
        up_left_direction = [(self.hor - s, self.ver - s) for s in range(1, min(self.hor, self.ver) + 1)]
        down_left_direction = [(self.hor + s, self.ver - s) for s in range(1, 8 - max(self.hor, 7 - self.ver))]
        down_right_direction = [(self.hor + s, self.ver + s) for s in range(1, 8 - max(self.hor, self.ver))]
        input_moves = [
            left_direction, right_direction, up_direction, down_direction,
            up_right_direction, up_left_direction, down_left_direction, down_right_direction
        ]
        for direction in input_moves:
            for hor, ver in direction:
                target = current_board[hor][ver]
                if isinstance(target, Piece) and self.color == target.color:
                    break
                elif isinstance(target, Piece) and self.color != target.color:
                    return True

    def is_defence(self):
        pass

    def is_checkmate(self, current_board):
        if self.is_check(current_board) and not self.moves_current_board(current_board) and not self.is_defence():
            return True

    def is_stalemate(self, current_board):
        if (not self.is_check(current_board) and not self.moves_current_board(current_board) and
                not self.any_moves(current_board)):
            return True