import global_vars

class PieceMovementValidation:
    def pieceHasSpaceToMove(from_coord, turn):
        i, j = from_coord

        if i >= 8 or i < 0 or j >= 8 or j < 0:
            return False

        vertical_direction = -1 if turn == 'w' else 1
        return global_vars.matrix[i+vertical_direction][j-1] is None or global_vars.matrix[i+vertical_direction][j+1] is None