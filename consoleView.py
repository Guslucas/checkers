class ConsoleView:
    LETTERS = 'ABCDEFGH'
    PIECES = [' ○ ', ' ● ']

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
        # Render piece
        if piece > 0:
            return ConsoleView.PIECES[piece-1]
        
        # Render chessboard pattern
        if (i%2 + j) % 2:
            return '   '
        return '███'

    def requestMovement():
        from_coord = ConsoleView.requestCoordinate('Digite a peça a ser movida: ')
        to_coord = ConsoleView.requestCoordinate('Digite o target: ')
        
        return from_coord, to_coord
    
    def requestCoordinate(msg):
        piece = input(msg)
        line_idx = piece[0]
        col_idx = int(piece[1])
        
        line_idx = ConsoleView.LETTERS.index(line_idx)
        col_idx -= 1

        return (line_idx, col_idx)