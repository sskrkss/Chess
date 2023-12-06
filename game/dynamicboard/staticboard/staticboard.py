from .pieces import *
import copy


# задача класса:
# 1) отрисовка стартовой доски с отображением самых важных ее характеристик (позиция, разноцветная разлиновка полей)
# 2) сохранение качественных характеристик текущей позиции с помощью аттрибутов в контексте шахматных правил
# 3) интерпретация текущей позиции с помощью тернарных функций в контексте шахматных правил
class StaticBoard:
    _row1 = [
        Rook(0, 0, 'b'), Knight(0, 1, 'b'), Bishop(0, 2, 'b'), Queen(0, 3, 'b'),
        King(0, 4, 'b'), Bishop(0, 5, 'b'), Knight(0, 6, 'b'), Rook(0, 7, 'b')
    ]
    _row2 = [Pawn(1, v, 'b') for v in range(8)]
    _row3 = [EmptyCell(2, v) for v in range(8)]
    _row4 = [EmptyCell(3, v) for v in range(8)]
    _row5 = [EmptyCell(4, v) for v in range(8)]
    _row6 = [EmptyCell(5, v) for v in range(8)]
    _row7 = [Pawn(6, v, 'w') for v in range(8)]
    _row8 = [
        Rook(7, 0, 'w'), Knight(7, 1, 'w'), Bishop(7, 2, 'w'), Queen(7, 3, 'w'),
        King(7, 4, 'w'), Bishop(7, 5, 'w'), Knight(7, 6, 'w'), Rook(7, 7, 'w')
    ]
    _start_board = [_row1, _row2, _row3, _row4, _row5, _row6, _row7, _row8]

    def __init__(self):
        self.board = self._start_board  # текущая позиция на доске
        self.turn = 'w'  # очередность хода
        self.last_move = [None, False]  # последняя фигура, совершившая ход, а также факт взятия
        self.king_coord = {'w': (7, 4), 'b': (0, 4)}  # текущая позиция королей
        self.triple_repetition_counter = []
        self.fifty_moves_counter = 0  # текущее количество ходов без взятия и хода пешкой

    def __str__(self):
        return '\n'.join(' '.join(str(c).center(4) for c in h) for h in self.board)

    def __repr__(self):
        return '\n'.join(' '.join(repr(c).ljust(15) for c in h) for h in self.board)

    # выбранная клетка - фигура или нет
    def is_piece(self, hor, ver):
        return isinstance(self.board[hor][ver], Piece)

    # выбранная фигура - ее ход или нет
    def is_turn(self, hor, ver):
        return self.board[hor][ver].color == self.turn

    # выбранная клетка под боем или нет
    def is_fire(self, hor, ver):
        input_moves = Queen(hor, ver, self.turn).moves_empty_board()
        for direction in input_moves:
            for h, v in direction:
                if self.is_piece(h, v):
                    if self.is_turn(h, v):
                        break
                    else:
                        if any([(hor, ver) in opposite for opposite in self.board[h][v].moves_empty_board()]):
                            return True

    # король под шахом или нет
    def is_check(self):
        h, v = self.king_coord[self.turn]
        return self.is_fire(h, v)

    # возможна ли короткая рокировка
    def is_short_castling(self, turn=''):
        if turn:
            h, v = self.king_coord[turn]
        else:
            h, v = self.king_coord[self.turn]
        if (not self.board[h][v].previous_coord and not self.board[h][7].previous_coord and
                all([not self.is_piece(h, x) for x in range(5, 7)]) and
                all([not self.is_fire(h, x) for x in range(4, 7)])):
            return h, 6

    # возможна ли длинная рокировка
    def is_long_castling(self, turn=''):
        if turn:
            h, v = self.king_coord[turn]
        else:
            h, v = self.king_coord[self.turn]
        if (not self.board[h][v].previous_coord and not self.board[h][0].previous_coord and
                all([not self.is_piece(h, x) for x in range(1, 4)]) and
                all([not self.is_fire(h, x) for x in range(2, 5)])):
            return h, 2

    # возможные ходы выбранной фигуры без учета блокировки от шаха
    def possible_moves(self, hor, ver):
        selected_square = self.board[hor][ver]
        input_moves = selected_square.moves_empty_board()
        output_moves = []
        # bishop, queen, rook, knight, king
        if isinstance(selected_square, (Bishop, Queen, Rook, Knight, King)):
            for direction in input_moves:
                for h, v in direction:
                    target = self.board[h][v]
                    if target.__class__ is EmptyCell:
                        output_moves.append((h, v))
                    else:
                        if selected_square.color != target.color:
                            output_moves.append((h, v))
                        break
        # pawn
        elif selected_square.__class__ is Pawn:
            updown_direction, diag_direction = input_moves
            # вертикальные ходы
            for h, v in updown_direction:
                target = self.board[h][v]
                if target.__class__ is EmptyCell:
                    output_moves.append((h, v))
                else:
                    break
            # диагональные взятия
            for h, v in diag_direction:
                target = self.board[h][v]
                if isinstance(target, Piece) and self.turn != target.color:
                    output_moves.append((h, v))
            # взятие на проходе
            for h, v in diag_direction:
                target = self.board[selected_square.hor][v]
                if (target.__class__ is Pawn and self.turn != target.color and
                        abs(selected_square.hor - target.previous_coord[0]) == 2 and
                        target == self.last_move[0]):
                    output_moves.append((h, v))
        return output_moves

    # финальные ходы выбранной фигуры с учетом блокировки от шаха
    def final_moves(self, hor, ver):
        output_moves = []
        for h2, v2 in self.possible_moves(hor, ver):
            backup = copy.deepcopy(self.board)
            self.board[h2][v2] = self.board[hor][ver]  # передвигаем фигуру
            self.board[hor][ver] = EmptyCell(hor, ver)  # освобождаем предыдущую клетку
            self.board[h2][v2].after_move(h2, v2)  # записываем новые координаты фигуры
            if self.board[h2][v2].__class__ is King:
                self.king_coord[self.board[h2][v2].color] = h2, v2  # записываем новые координаты короля для доски
            if not self.is_check():
                output_moves.append((h2, v2))
            if self.board[h2][v2].__class__ is King:
                self.king_coord[self.board[h2][v2].color] = hor, ver  # записываем новые координаты короля для доски
            self.board[h2][v2].after_move(hor, ver)  # записываем старые координаты фигуры
            self.board = backup  # возвращаем старую доску
        return output_moves

    def all_final_moves(self):
        output_moves = []
        for h in range(8):
            for v in range(8):
                if self.is_piece(h, v):
                    output_moves.append(self.final_moves(h, v))
        return output_moves

    # вспомогательные функции для определения возможности выхода из event loop
    # 1) возникла ли позиция невозможности любого хода (пат/мат)
    def is_no_moves(self):
        for h in range(8):
            for v in range(8):
                if self.is_piece(h, v) and self.is_turn(h, v) and self.final_moves(h, v):
                    return
        return True

    # 2) находится ли король под шахом при одновременной невозможности любого хода (мат)
    def is_checkmate(self):
        return self.is_check() and self.is_no_moves()

    # 3) возникла ли позиция невозможности мата по причине недостатка фигур
    def is_no_pieces(self):
        knight_scores = {'w': 0, 'b': 0}
        bishop_scores = {'w': {'w': False, 'b': False}, 'b': {'w': False, 'b': False}}
        for h in range(8):
            for v in range(8):
                square = self.board[h][v]
                if isinstance(square, (Pawn, Queen, Rook)):
                    return
                elif square.__class__ is Knight:
                    knight_scores[square.color] += 1
                elif square.__class__ is Bishop:
                    bishop_scores[square.color][square.square] = True
        total_white_scores = knight_scores['w'] + sum(bishop_scores['w'].values())
        total_black_scores = knight_scores['b'] + sum(bishop_scores['b'].values())
        return total_white_scores < 2 and total_black_scores < 2

    # 4) повторилась ли позиция 3 раза при одной и той же очередности хода и одинаковых возможных ходов (доработать)
    def is_triple_repetition(self):
        all_moves = self.all_final_moves()
        all_moves.append(
            [self.is_short_castling('w'), self.is_long_castling('w'),
             self.is_short_castling('b'), self.is_long_castling('b')]
        )
        position = [[p.__str__() for p in row] for row in self.board]
        self.triple_repetition_counter.append((all_moves, position, self.turn))
        return self.triple_repetition_counter.count((all_moves, position, self.turn)) == 3

    # 5) счетчик ходов без взятия и без хода пешкой
    def is_fifty_moves(self):
        if self.last_move[0].__class__ is Pawn or self.last_move[1]:
            self.fifty_moves_counter = 0
        else:
            self.fifty_moves_counter += 1
        return self.fifty_moves_counter == 50
