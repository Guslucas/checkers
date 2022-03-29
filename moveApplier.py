import global_vars
from coordinateTranslator import CoordinateTranslator
from consoleView import ConsoleView
import time

from pieces.king import King

class MoveApplier:
    def apply(move, move_str, turn, show_every_move = False, is_cpu = False):
        _from = move_str[0:2]
        piece = move[3]
        
        moves_qty = int((len(move_str) - 2) / 2)
        for i in range(moves_qty):
            _to = move_str[2 + i*2:4 + i *2]
            
            from_idx = ConsoleView.coordinateToIndex(_from)
            to_idx = ConsoleView.coordinateToIndex(_to)
            MoveApplier.move_piece(piece, from_idx, to_idx, turn)

            if show_every_move:
                ConsoleView.showCheckers()
                time.sleep(.5)
                if is_cpu and turn == 'b' and i < moves_qty:
                    time.sleep(.5)


            _from = _to
        
        last_i, _ = to_idx

        if last_i == 0 and piece.color == 'w':
            piece.promote_to_king()
            return
        
        if last_i == 7 and piece.color == 'b':
            piece.promote_to_king()


    def move_piece(piece, _from, _to, turn):
        matrix = global_vars.matrix

        from_i, from_j = _from
        to_i, to_j = _to

        if turn == 'w':
            di = to_i - from_i
            dj = to_j - from_j
        else:
            di = from_i - to_i
            dj = from_j - to_j
        
        if isinstance(piece, King):
            
            enemy_i = None
            enemy_j = None

            # walk until see a piece
            steps = 1
            direction = {'i': -1 if di < 0 else 1, 'j': -1 if dj < 0 else 1}
            while True:
                can_move = piece.place_moving(from_i, from_j, turn, direction, steps, matrix)

                place_at_board, new_i, new_j = can_move

                if steps >= abs(di):
                    break

                # out of the board
                if place_at_board == False:
                    break
                
                if place_at_board is not None:
                    enemy_i = new_i
                    enemy_j = new_j
                    break
                
                steps += 1
                
            # If saw an enemy, search for other or end of board, to calculate possible movement
            matrix[to_i][to_j] = matrix[from_i][from_j]
            matrix[from_i][from_j] = None
            
            if enemy_i:
                matrix[enemy_i][enemy_j] = None

                

        else:
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