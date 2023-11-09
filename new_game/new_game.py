from .chessrules import *


class NewGame(ChessRules):
    _dict_ver = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    _dict_hor = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    def __init__(self):
        super().__init__()
        self.game_status = 'in progress'

    def converter(self, coord):
        return self._dict_hor[coord[1]], self._dict_ver[coord[0]]

    def new_game(self):
        while True:
            print(self)
            print()
            print('Ход белых')
            print()
            h1, v1 = self.converter(input().lower())
            h2, v2 = self.converter(input().lower())
            if not self.move(h1, v1, h2, v2, 'w'):
                break
        while True:
            print(self)
            print()
            print('Ход черных')
            print()
            h1, v1 = self.converter(input().lower())
            h2, v2 = self.converter(input().lower())
            if not self.move(h1, v1, h2, v2, 'b'):
                break