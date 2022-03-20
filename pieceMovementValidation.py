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
        
        coord_left.moveDiag(1, CoordinateTranslator.TOP_LEFT)
        coord_right.moveDiag(1, CoordinateTranslator.TOP_RIGHT)

        # Normalizing black pieces
        coord_left.translateIfNeeded()
        coord_right.translateIfNeeded()
        

        top_left_1 = global_vars.matrix[coord_left.i][coord_left.j]
        top_right_1 = global_vars.matrix[coord_right.i][coord_right.j]
        
        if top_left_1 is None or top_right_1 is None:
            return True
        
        coord_left_2 = CoordinateTranslator(turn, i, j)
        coord_right_2 = CoordinateTranslator(turn, i, j)
        
        # Normalizing black pieces
        coord_left_2.translateIfNeeded()
        coord_right_2.translateIfNeeded()
        
        coord_left_2.moveDiag(2, CoordinateTranslator.TOP_LEFT)
        coord_right_2.moveDiag(2, CoordinateTranslator.TOP_RIGHT)

        # Normalizing black pieces
        coord_left_2.translateIfNeeded()
        coord_right_2.translateIfNeeded()
        

        top_left_2 = global_vars.matrix[coord_left_2.i][coord_left_2.j]
        top_right_2 = global_vars.matrix[coord_right_2.i][coord_right_2.j]

        # can capture
        if top_left_1.color != turn and top_left_2 is None or \
            top_right_1.color != turn and top_right_2 is None:
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
        
        