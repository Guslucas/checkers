class ConsoleView:
    def showCheckers(matrix):
        for i in range(0, 8):
            linha = ''
            for j in range(0, 8):
                linha += ConsoleView.renderPiece(matrix[i][j], i, j)
            print(linha)

    def renderPiece(piece, i, j):
        if piece == 1:
            return '░░'
        
        if piece == 2:
            return '▒▒'
        
        return '██'