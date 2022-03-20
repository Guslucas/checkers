from placeOnBoardValidation import PlaceOnBoardValidation
import global_vars
class CoordinateTranslator:

    TOP_LEFT = {'i': -1, 'j': -1}
    TOP_RIGHT = {'i': -1, 'j': 1}
    BOTTOM_LEFT = {'i': 1, 'j': -1}
    BOTTOM_RIGHT = {'i': 1, 'j': 1}
    DIRECTIONS = [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]   

    def __init__(self, turn, i, j):
        self.color = turn
        self.i = i
        self.j = j
        self.valid = True
        # Normalizing black pieces
        self.translateIfNeeded()

    def translateIfNeeded(self):
        if self.color == 'b':
            self.translate()

    def translate(self):
        self.i = abs(self.i - 7)
        self.j = abs(self.j - 7)
        print('new i, j = ', self.i, self.j)

    def moveDiag(self, places_qty, direction):
        if direction not in CoordinateTranslator.DIRECTIONS:
            raise ValueError(f"Invalid driection {direction}.")
        
        target_i = self.i + (places_qty * direction['i'])
        target_j = self.j + (places_qty * direction['j'])
        
        if PlaceOnBoardValidation.isOnBoard((target_i, target_j)):
            self.i = target_i
            self.j = target_j
            
            # Normalizing black pieces
            self.translateIfNeeded()

            return True
        else:
            self.valid = False
            self.i = None
            self.j = None

            # Normalizing black pieces
            return False
        
    def placeAtBoard(self):
        if not self.valid:
            return None
        return global_vars.matrix[self.i][self.j]