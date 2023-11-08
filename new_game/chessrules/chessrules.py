from .board import *


class ChessRules(Board):
    def move(self, h1, v1, h2, v2, turn):
        selected_cell = self.board[h1][v1]
        if isinstance(selected_cell, Piece) and selected_cell.color == turn:

            #  обычный ход
            if (h2, v2) in selected_cell.moves_current_board(self.board):
                self.board[h1][v1].previous_coord = h1, v1  # записываем предыдущие координаты фигуры
                self.board[h2][v2] = self.board[h1][v1]
                self.board[h1][v1] = EmptyCell(h1, v1)
                self.last_move = self.board[h2][v2]  # записываем фигуру, ходившую последней

            #  рокировка в короткую сторону
            elif isinstance(selected_cell, King) and (h2, v2) in selected_cell.short_castling(self.board):
                h = h2
                self.board[h][4].previous_coord = h, 4  # записываем предыдущие координаты фигуры
                self.board[h][5] = self.board[h][7]
                self.board[h][6] = self.board[h][4]
                self.board[h][4] = EmptyCell(h, 4)
                self.board[h][7] = EmptyCell(h, 7)
                self.last_move = self.board[h][6]  # записываем фигуру, ходившую последней

            #  рокировка в длинную сторону
            elif isinstance(selected_cell, King) and (h2, v2) in selected_cell.long_castling(self.board):
                h = h2
                self.board[h][4].previous_coord = h, 4  # записываем предыдущие координаты фигуры
                self.board[h][2] = self.board[h][4]
                self.board[h][3] = self.board[h][0]
                self.board[h][0] = EmptyCell(h, 0)
                self.board[h][1] = EmptyCell(h, 1)
                self.board[h][4] = EmptyCell(h, 4)
                self.last_move = self.board[h][2]  # записываем фигуру, ходившую последней

            else:
                print('Такого хода нет. Попробуйте еще раз')
                return True
        else:
            print('Вы выбрали пустую клетку или чужую фигуру. Попробуйте еще раз')
            return True