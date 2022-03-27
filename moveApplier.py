import global_vars
from coordinateTranslator import CoordinateTranslator
from consoleView import ConsoleView
import time

class MoveApplier:
    def apply(move, move_str, turn, show_every_move = False, is_cpu = False):
        _from = move_str[0:2]
        
        moves_qty = int((len(move_str) - 2) / 2)
        for i in range(moves_qty):
            _to = move_str[2 + i*2:4 + i *2]
            
            from_idx = ConsoleView.coordinateToIndex(_from)
            to_idx = ConsoleView.coordinateToIndex(_to)
            MoveApplier.move_piece(from_idx, to_idx, turn)

            if show_every_move:
                ConsoleView.showCheckers()
                time.sleep(.5)
                if is_cpu and turn == 'b' and i < moves_qty:
                    time.sleep(.5)


            _from = _to
        
        piece = move[3]
        last_i, _ = to_idx

        if last_i == 0 and piece.color == 'w':
            piece.promote_to_king()
            return
        
        if last_i == 7 and piece.color == 'b':
            piece.promote_to_king()


    def move_piece(_from, _to, turn):
        matrix = global_vars.matrix

        from_i, from_j = _from
        to_i, to_j = _to

        if turn == 'w':
            di = to_i - from_i
            dj = to_j - from_j
        else:
            di = from_i - to_i
            dj = from_j - to_j

        # not capturing
        if abs(di) == 1 and abs(dj == 1):
            #moving
            el = CoordinateTranslator(turn, from_i, from_j, matrix)
            el.i += di
            el.j += dj
            el.translateIfNeeded()

            matrix[el.i][el.j] = matrix[from_i][from_j]
            matrix[from_i][from_j] = None
            return

        # capturing
        el = CoordinateTranslator(turn, from_i, from_j, matrix)
        el.i += int(di / 2)
        el.j += int(dj / 2)
        el.translateIfNeeded()

        el2 = CoordinateTranslator(turn, from_i, from_j, matrix)
        el2.i += di
        el2.j += dj
        el2.translateIfNeeded()

        matrix[el2.i][el2.j] = matrix[from_i][from_j]
        matrix[el.i][el.j] = None
        matrix[from_i][from_j] = None