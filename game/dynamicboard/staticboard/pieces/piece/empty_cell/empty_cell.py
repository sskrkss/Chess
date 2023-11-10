class EmptyCell:
    _dict_ver = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, hor, ver):
        self.ver = ver
        self.hor = hor
        self.coord = f'{self._dict_ver[ver]}{8-hor}'
        self.square = 'wb'[(ver + hor) % 2]

    def __str__(self):
        return '*'

    def __repr__(self):
        return f'EmptyCell({self.hor}, {self.ver})'

    def after_move(self, hor, ver):
        self.ver = ver
        self.hor = hor
        self.coord = f'{self._dict_ver[ver]}{8 - hor}'
        self.square = 'wb'[(ver + hor) % 2]
