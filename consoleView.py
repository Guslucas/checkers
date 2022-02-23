class ConsoleView:
    LETTERS = 'ABCDEFGH'

    def showCheckers(matrix):
        linha = '  '
        for col_idx in '12345678':
            linha += f' {col_idx} '
        print(linha)

        for i in range(0, 8):
            linha = ''
            for j in range(0, 8):
                linha += ConsoleView.renderPiece(matrix[i][j], i, j)
            
            line_idx = ConsoleView.LETTERS[i]
            print(line_idx + ' ' + linha)

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
    

    def requestMovement():
        line_idx, col_idx = ConsoleView.requestCoordinate('Digite a peça a ser movida: ')
        print(line_idx, col_idx, sep=',')

        line_idx, col_idx = ConsoleView.requestCoordinate('Digite o target: ')
        print(line_idx, col_idx, sep=',')
        
    
    def requestCoordinate(msg):
        piece = input(msg)
        line_idx = piece[0]
        col_idx = int(piece[1])
        
        line_idx = ConsoleView.LETTERS.index(line_idx)
        col_idx -= 1

        return line_idx, col_idx