from operator import truediv

class PieceSelectionValidation:

  MATRIX = None

  def load(matrix):
    PieceSelectionValidation.MATRIX = matrix

  def isSelectedPieceValid(from_coord, current_turn):
    i, j = from_coord

    if i >= 8 or i < 0 or j >= 8 or j < 0:
      return False

    if PieceSelectionValidation.MATRIX[i][j] == current_turn:
      return True

    return False
