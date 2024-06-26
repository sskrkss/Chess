from .staticboard import *


class DynamicBoard(StaticBoard):
    _piece_promotion = {'q': Queen, 'n': Knight, 'b': Bishop, 'r': Rook}

    def move(self, h1, v1, h2, v2):  # вынести в отдельный интерфейс
        selected_cell = self.board[h1][v1]
        # обычный ход
        if (h2, v2) in self.final_moves(h1, v1):
            self.last_move = [self.board[h1][v1], self.is_piece(h2, v2)]  # записываем ходившую фигуру и факт взятия
            self.board[h2][v2] = self.board[h1][v1]  # передвигаем фигуру
            self.board[h1][v1] = EmptyCell(h1, v1)  # освобождаем предыдущую клетку
            self.board[h2][v2].previous_coord = h1, v1  # записываем предыдущие координаты фигуры
            self.board[h2][v2].after_move(h2, v2)  # записываем новые координаты фигуры
            self.last_move[0] = self.board[h2][v2]  # записываем фигуру, ходившую последней
            if self.board[h2][v2].__class__ is King:
                self.king_coord[self.turn] = h2, v2  # записываем новые координаты короля для доски
        # рокировка в короткую сторону
        elif selected_cell.__class__ is King and (h2, v2) == self.is_short_castling():
            h = h2
            self.board[h][7].previous_coord = h, 7  # записываем предыдущие координаты ладьи
            self.board[h][4].previous_coord = h, 4  # записываем предыдущие координаты короля
            self.board[h][5] = self.board[h][7]  # передвигаем ладью
            self.board[h][5].after_move(h, 5)  # записываем новые координаты ладьи
            self.board[h][6] = self.board[h][4]  # передвигаем короля
            self.board[h][6].after_move(h, 6)  # записываем новые координаты короля
            self.board[h][4] = EmptyCell(h, 4)  # освобождаем предыдущую клетку
            self.board[h][7] = EmptyCell(h, 7)  # освобождаем предыдущую клетку
            self.last_move = self.board[h][6], False  # записываем фигуру, ходившую последней и факт взятия
            self.king_coord[self.turn] = h2, v2  # записываем новые координаты короля для доски
        # рокировка в длинную сторону
        elif selected_cell.__class__ is King and (h2, v2) == self.is_long_castling():
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
            self.last_move = self.board[h][2], False  # записываем фигуру, ходившую последней и факт взятия
            self.king_coord[self.turn] = h2, v2  # записываем новые координаты короля для доски
        else:
            print('Такого хода нет. Попробуйте еще раз')
            return
        return True

    def pawn_promotion(self, h2, v2, turn):
        if self.board[h2][v2].__class__ is Pawn and not h2 % 7:
            while True:
                print('Выберите фигуру для превращения пешки: q, n , b, r')
                try:
                    self.board[h2][v2] = self._piece_promotion[input()](h2, v2, turn)
                except KeyError:
                    print('Такой фигуры нет. Попробуйте еще раз')
                    continue
                break
