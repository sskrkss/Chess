from .empty_cell import EmptyCell

class Figure(EmptyCell):
    def __init__(self, hor, ver, color):
        super().__init__(hor, ver)
        self.color = color