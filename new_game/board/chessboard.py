from new_game.pieces import *

class ChessBoard:
    def __init__(self):
        row1 = [
            Rook(0, 0, 'b'), Knight(0, 1, 'b'), Bishop(0, 2, 'b'), Queen(0, 4, 'b'),
            King(0, 3, 'b'), Bishop(0, 5, 'b'), Knight(0, 6, 'b'), Rook(0, 7, 'b')
        ]
        row2 = [Pawn(1, v, 'b') for v in range(8)]
        row3 = [EmptyCell(2, v) for v in range(8)]
        row4 = [EmptyCell(3, v) for v in range(8)]
        row5 = [EmptyCell(4, v) for v in range(8)]
        row6 = [EmptyCell(5, v) for v in range(8)]
        row7 = [Pawn(6, v, 'w') for v in range(8)]
        row8 = [
            Rook(7, 0, 'w'), Knight(7, 1, 'w'), Bishop(7, 2, 'w'), King(7, 3, 'w'),
            Queen(7, 4, 'w'), Bishop(7, 5, 'w'), Knight(7, 6, 'w'), Rook(7, 7, 'w')
        ]
        self.board = [row1, row2, row3, row4, row5, row6, row7, row8]

    def __str__(self):
        return '\n'.join(' '.join(str(c) for c in h) for h in self.board)

    def __repr__(self):
        return '\n'.join(' '.join(repr(c).ljust(15) for c in h) for h in self.board)

    def show_coord(self):
        return '\n'.join(' '.join(c.coord for c in h) for h in self.board)

    def show_square(self):
        return '\n'.join(' '.join(c.square for c in h) for h in self.board)

    def move(self, h1, v1, h2, v2, turn):
        selected_cell = self.board[h1][v1]
        if isinstance(selected_cell, Figure) and selected_cell.color == turn:
            if (h2, v2) in selected_cell.moves_current_board(self.board):
                self.board[h2][v2] = self.board[h1][v1]
                self.board[h1][v1] = EmptyCell(h1, v1)
            else:
                print('Такого хода нет. Попробуйте еще раз')
                return True
        else:
            print('Вы выбрали пустую клетку или чужую фигуру. Попробуйте еще раз')
            return True