class Piece:
    ALLOWED_COLORS = ['b', 'w']
    SYMBOLS = ' ○ ', ' ● '

    def __init__(self, color):
        if color not in self.ALLOWED_COLORS:
            raise ValueError(f"Invalid color {color}.")
        self.color = color
        self.symbol = Piece.SYMBOLS[0 if color == 'b' else 1]
    
    def __repr__(self):
        return self.symbol