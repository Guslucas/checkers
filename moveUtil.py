from placeOnBoardValidation import PlaceOnBoardValidation
class MoveUtil:
    TOP_LEFT = {'i': -1, 'j': -1}
    TOP_RIGHT = {'i': -1, 'j': 1}
    BOTTOM_LEFT = {'i': 1, 'j': -1}
    BOTTOM_RIGHT = {'i': 1, 'j': 1}
    DIRECTIONS = [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]

    def moveDiag(i, j, places_qty, direction):
        if direction not in MoveUtil.DIRECTIONS:
            raise ValueError(f"Invalid driection {direction}.")
        
        target_i = i + (places_qty * direction['i'])
        target_j = j + (places_qty * direction['j'])
        
        if PlaceOnBoardValidation.isOnBoard((target_i, target_j)):
            return (target_i, target_j)
        else:
            raise ValueError(f"Out of the board.")
        
            