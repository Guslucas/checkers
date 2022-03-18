import global_vars
class PieceMovementValidation:
    def pieceHasSpaceToMove(from_coord, turn):
        i, j = from_coord

        vertical_direction = -1 if turn == 'w' else 1
        return global_vars.matrix[i+vertical_direction][j-1] is None or global_vars.matrix[i+vertical_direction][j+1] is None
    
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
        
        