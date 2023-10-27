from .board import *

class NewGame(ChessBoard):
    def select(self, hor, ver):
        selected_cell = self.board[hor][ver]
        print(selected_cell)
        if isinstance(selected_cell, Figure):
            input_moves = selected_cell.possible_moves()
            print(input_moves)
            output_moves = []
            if type(input_moves[0]) is tuple:
                for h, v in input_moves:
                    if type(self.board[h][v]) == EmptyCell:
                        output_moves.append((h, v))
            else:
                for direction in input_moves:
                    for h, v in direction:
                        if type(self.board[h][v]) == EmptyCell:
                            output_moves.append((h, v))
                        else:
                            break
        return output_moves