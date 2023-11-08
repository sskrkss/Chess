from .board import *


class ChessRules(Board):
    def move(self, h1, v1, h2, v2, turn):
        selected_cell = self.board[h1][v1]
        if isinstance(selected_cell, Piece) and selected_cell.color == turn:
            if (h2, v2) in selected_cell.moves_current_board(self.board):
                self.board[h1][v1].previous_coord = h1, v1  # записываем предыдущие координаты фигуры
                self.board[h2][v2] = self.board[h1][v1]
                self.board[h1][v1] = EmptyCell(h1, v1)
                self.last_move = self.board[h2][v2]  # записываем фигуру, ходившую последней
            else:
                print('Такого хода нет. Попробуйте еще раз')
                return True
        else:
            print('Вы выбрали пустую клетку или чужую фигуру. Попробуйте еще раз')
            return True