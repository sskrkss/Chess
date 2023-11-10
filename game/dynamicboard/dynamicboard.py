from .staticboard import *


class DynamicBoard(StaticBoard):
    def __init__(self):
        super().__init__()
        self.fifty_moves_counter = 0
        self.last_move = None

    def move(self, h1, v1, h2, v2, turn):
        selected_cell = self.board[h1][v1]
        if isinstance(selected_cell, Piece) and selected_cell.color == turn:
            #  обычный ход
            if (h2, v2) in selected_cell.moves_current_board(self.board):
                self.board[h2][v2] = self.board[h1][v1]  # передвигаем фигуру
                self.board[h1][v1] = EmptyCell(h1, v1)  # освобождаем предыдущую клетку
                self.board[h2][v2].previous_coord = h1, v1  # записываем предыдущие координаты фигуры
                self.board[h2][v2].after_move(h2, v2)  # записываем новые координаты фигуры
                self.last_move = self.board[h2][v2]  # записываем фигуру, ходившую последней
            #  рокировка в короткую сторону
            elif isinstance(selected_cell, King) and (h2, v2) == selected_cell.short_castling(self.board):
                h = h2
                self.board[h][7].previous_coord = h, 7  # записываем предыдущие координаты ладьи
                self.board[h][4].previous_coord = h, 4  # записываем предыдущие координаты короля
                self.board[h][5] = self.board[h][7]  # передвигаем ладью
                self.board[h][5].after_move(h, 5)  # записываем новые координаты ладьи
                self.board[h][6] = self.board[h][4]  # передвигаем короля
                self.board[h][6].after_move(h, 6)  # записываем новые координаты короля
                self.board[h][4] = EmptyCell(h, 4)  # освобождаем предыдущую клетку
                self.board[h][7] = EmptyCell(h, 7)  # освобождаем предыдущую клетку
                self.last_move = self.board[h][6]  # записываем фигуру, ходившую последней
            #  рокировка в длинную сторону
            elif isinstance(selected_cell, King) and (h2, v2) == selected_cell.long_castling(self.board):
                h = h2
                self.board[h][0].previous_coord = h, 0  # записываем предыдущие координаты ладьи
                self.board[h][4].previous_coord = h, 4  # записываем предыдущие координаты короля
                self.board[h][2] = self.board[h][4]  # записываем новые координаты короля
                self.board[h][2].after_move(h, 2)  # записываем новые координаты короля
                self.board[h][3] = self.board[h][0]  # записываем новые координаты ладьи
                self.board[h][3].after_move(h, 3)  # записываем новые координаты ладьи
                self.board[h][0] = EmptyCell(h, 0)  # освобождаем предыдущую клетку
                self.board[h][1] = EmptyCell(h, 1)  # освобождаем предыдущую клетку
                self.board[h][4] = EmptyCell(h, 4)  # освобождаем предыдущую клетку
                self.last_move = self.board[h][2]  # записываем фигуру, ходившую последней
            else:
                print('Такого хода нет. Попробуйте еще раз')
                return True
        else:
            print('Вы выбрали пустую клетку или чужую фигуру. Попробуйте еще раз')
            return True

    def fifty_moves_rule(self):
        if isinstance(self.last_move, Pawn):
            self.fifty_moves_counter = 0
        else:
            self.fifty_moves_counter += 1
