from .dynamicboard import *


class Game(DynamicBoard):
    _dict_ver = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    _dict_hor = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    _interface = {
        'w': 'Ход белых', 'b': 'Ход черных', 'wl': 'Черные выиграли. Мат', 'bl': 'Белые выиграли. Мат',
        'ds': 'Ничья. Пат', 'dp': 'Ничья. Недостаточно фигур для мата', 'dt': 'Ничья. Троекратное повторение ходов',
        'df': 'Ничья. Правило 50 ходов'
    }

    def __init__(self):
        super().__init__()
        self.status = self._interface[self.turn]

    def coord_converter(self, coord):
        return self._dict_hor[coord[1]], self._dict_ver[coord[0]]

    def cycle(self):
        while True:
            # 1 показываем текущую позицию на доске
            print(self, end='\n\n')

            # 2 сценарии выхода из event loop
            # 2.1 сценарий мата
            if self.is_checkmate(self):
                self.status = self._interface[f'{self.turn}l']
                return

            # 2.2 сценарий пата
            if self.is_stalemate(self):
                self.status = self._interface['ds']
                return

            # 2.3 сценарий недостатка фигур для мата
            if not self.is_enough_pieces():
                self.status = self._interface['dp']
                return

            # 2.4 троекратного повторения ходов
            if self.is_triple_repetition():
                self.status = self._interface['dt']
                return

            # 2.5 сценарий реализации правила 50 ходов
            if self.is_fifty_moves_rule():
                self.status = self._interface['df']
                return

            # 3 если выход из event loop не происходит, делаем ход
            print(self.status)
            while True:
                print('Введите координаты выбранной фигуры')
                h1, v1 = self.coord_converter(input().lower())
                if not self.is_piece(h1, v1) or not self.is_turn(h1, v1):
                    continue
                print('Введите координаты хода')
                h2, v2 = self.coord_converter(input().lower())
                if self.move(h1, v1, h2, v2, self.turn):
                    break

            # 4 меняем ход
            if self.turn == 'w':
                self.turn = 'b'
            else:
                self.turn = 'w'
            self.status = self._interface[self.turn]
