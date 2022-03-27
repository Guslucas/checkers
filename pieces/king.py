from pieces.piece import Piece

class King(Piece):

    SYMBOLS = ['♚', ' ♔ ']

    def __init__(self, color):
        pass
    
    def update_symbol(self):
        self.symbol = King.SYMBOLS[self.ALLOWED_COLORS.index(self.color)]