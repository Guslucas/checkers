import global_vars
from coordinateTranslator import CoordinateTranslator
class PieceMovementValidation:
    def pieceHasSpaceToMove(from_coord, turn):
        i, j = from_coord
        
        coord_left = CoordinateTranslator(turn, i, j)
        coord_right = CoordinateTranslator(turn, i, j)
        
        coord_left.moveDiag(1, CoordinateTranslator.TOP_LEFT)
        coord_right.moveDiag(1, CoordinateTranslator.TOP_RIGHT)
        
        if coord_left.placeAtBoard() is None or coord_right.placeAtBoard() is None:
            return True
        
        coord_left_2 = CoordinateTranslator(turn, i, j)
        coord_right_2 = CoordinateTranslator(turn, i, j)
        
        coord_left_2.moveDiag(2, CoordinateTranslator.TOP_LEFT)
        coord_right_2.moveDiag(2, CoordinateTranslator.TOP_RIGHT)

        # can capture
        if coord_left.placeAtBoard().color != turn and coord_left_2.placeAtBoard() is None or \
            coord_right.placeAtBoard().color != turn and coord_left_2.placeAtBoard() is None:
            return True

        return 
    
    def isValidMovement(from_coord, to_coord, turn):
        fi, fj = from_coord
        ti, tj = to_coord
        
        di = ti - fi
        dj = tj -fj
        
        if di == 0 or dj == 0:
            return False

        if turn == 'w' and di > 0:
            return False
        
        if turn == 'b' and di < 0:
            return False
        
        if abs(di) > 1 or abs(dj) > 1:
            return False
        
        return global_vars.matrix[ti][tj] is None or global_vars.matrix[ti][tj] is None
        
        