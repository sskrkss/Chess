from .empty_cell import *


class Piece(EmptyCell):
    def __init__(self, hor, ver, color):
        super().__init__(hor, ver)
        self.color = color
        self.previous_coord = None

    def moves_empty_board(self):
        return None
