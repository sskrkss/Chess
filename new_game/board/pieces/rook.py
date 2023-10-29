from .empty_cell import EmptyCell
from .figure import Figure

class Rook(Figure):
    def __str__(self):
        return 'R'

    def __repr__(self):
        return f'Rook({self.hor}, {self.ver})'

    def moves_empty_board(self):
        left_direction = [(self.hor, v) for v in range(self.ver - 1, -1, -1)]
        right_direction = [(self.hor, v) for v in range(self.ver + 1, 8)]
        up_direction = [(h, self.ver) for h in range(self.hor - 1, -1, -1)]
        down_direction = [(h, self.ver) for h in range(self.hor + 1, 8)]
        return [left_direction, right_direction, up_direction, down_direction]

    def moves_current_board(self, current_board):
        input_moves = self.moves_empty_board()
        output_moves = []
        for direction in input_moves:
            for hor, ver in direction:
                target = current_board[hor][ver]
                if type(target) == EmptyCell:
                    output_moves.append((hor, ver))
                else:
                    if self.color != target.color:
                        output_moves.append((hor, ver))
                    break
        return output_moves