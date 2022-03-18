from operator import truediv
import global_vars

class PieceSelectionValidation:

  def isSelectedPieceValid(from_coord, current_turn):
    i, j = from_coord
    
    if global_vars.matrix[i][j] is None:
      return False
    
    if global_vars.matrix[i][j].color == current_turn:
      return True

    return False
