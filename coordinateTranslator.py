class CoordinateTranslator:
    def __init__(self, turn, i, j):
        self.color = turn
        self.i = i
        self.j = j

    def translateIfNeeded(self):
        if self.color == 'b':
            self.translate()

    def translate(self):
        self.i = abs(self.i - 7)
        self.j = abs(self.j - 7)
        print('new i, j = ', self.i, self.j)
