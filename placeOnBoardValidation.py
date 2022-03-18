class PlaceOnBoardValidation:
    def isOnBoard(coord):
        i, j = coord
        return i < 8 and i >= 0 and j < 8 and j >= 0