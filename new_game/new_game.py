from .chessrules import *


class NewGame(ChessRules):
    def new_game(self):
        while True:
            while True:
                print(self)
                print()
                print('Ход белых')
                print()
                h1, v1, h2, v2 = [int(input()) for _ in range(4)]
                if not self.move(h1, v1, h2, v2, 'w'):
                    break
            while True:
                print(self)
                print()
                print('Ход черных')
                print()
                h1, v1, h2, v2 = [int(input()) for _ in range(4)]
                if not self.move(h1, v1, h2, v2, 'b'):
                    break