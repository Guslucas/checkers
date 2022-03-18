import global_vars
from coordinateTranslator import CoordinateTranslator
class PieceMovementValidation:
    def pieceHasSpaceToMove(from_coord, turn):
        i, j = from_coord
        
        coord_left = CoordinateTranslator(turn, i, j)
        coord_right = CoordinateTranslator(turn, i, j)
        
        # Normalizing black pieces
        coord_left.translateIfNeeded()
        coord_right.translateIfNeeded()
        
        coord_left.i -= 1
        coord_left.j -= 1

        coord_right.i -= 1
        coord_right.j += 1

        # Normalizing black pieces
        coord_left.translateIfNeeded()
        coord_right.translateIfNeeded()
        
        return global_vars.matrix[coord_left.i][coord_left.j] is None or global_vars.matrix[coord_right.i][coord_right.j] is None
    
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
        
        