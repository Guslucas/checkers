from operator import truediv
import global_vars

class PieceSelectionValidation:

  def isSelectedPieceValid(from_coord, current_turn):
    i, j = from_coord

    if i >= 8 or i < 0 or j >= 8 or j < 0:
      return False

    if global_vars.matrix[i][j] is None:
      return False
    
    if global_vars.matrix[i][j].color == current_turn:
      return True
