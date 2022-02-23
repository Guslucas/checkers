class ConsoleView:
    def showCheckers(matrix):
        linha = '  '
        for letter in 'ABCDEFGH':
            linha += f' {letter} '
        print(linha)

        for i in range(0, 8):
            linha = ''
            for j in range(0, 8):
                linha += ConsoleView.renderPiece(matrix[i][j], i, j)
            print(str(i+1) + ' ' + linha)

    def renderPiece(piece, i, j):
        if piece == 1:
            return ' ○ '
        
        if piece == 2:
            return ' ● '
        
        diff = 1
        if i%2==0:
            diff = 0

        if (diff + j) % 2:
            return '   '
        
        return '███'