import os
from placeOnBoardValidation import PlaceOnBoardValidation
from pieceSelectionValidation import PieceSelectionValidation
from pieceMovementValidation import PieceMovementValidation
import global_vars

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

class ConsoleView:
    LETTERS = 'ABCDEFGH'
    PIECES = [' ○ ', ' ● ']

    def showCheckers():
        clearConsole()
        linha = '  '
        for col_idx in '12345678':
            linha += f' {col_idx} '
        print(linha)

        for i in range(0, 8):
            linha = ''
            for j in range(0, 8):
                linha += ConsoleView.renderPiece(global_vars.matrix[i][j], i, j)
            
            line_idx = ConsoleView.LETTERS[i]
            print(line_idx + ' ' + linha)

    def renderPiece(piece, i, j):
        # Render piece
        if piece is not None:
            return piece.symbol
        
        # Render chessboard pattern
        if (i%2 + j) % 2:
            return '   '
        return '███'

    def requestMovement(current_turn):
        while True:
            from_coord = ConsoleView.requestCoordinate('Enter the piece coord: ')
            if PlaceOnBoardValidation.isOnBoard(from_coord) and \
                PieceSelectionValidation.isSelectedPieceValid(from_coord, current_turn) and \
                PieceMovementValidation.pieceHasSpaceToMove(from_coord, current_turn):
                break

            print('Oops.. This is not a valid selection for current turn. Try again.')
        
        while True:
            to_coord = ConsoleView.requestCoordinate('Enter target coord: ')
            if PlaceOnBoardValidation.isOnBoard(to_coord) and\
                PieceMovementValidation.isValidMovement(from_coord, to_coord, current_turn):
                break
            print('Oops.. This is not a valid movement.')
        
        return from_coord, to_coord
    
    def requestValidMove(possibleMoves, turn):
        while True:
            if turn == 'w':
                move_str = input(turn + " - Enter the string containing the play: (ex: 'B7D5F7')\n_> ")
            else:
                move_str = possibleMoves[0][0][0]
            move_found = [el[1] for el in enumerate(possibleMoves) if move_str in el[1][0]]
            
            #if empty
            if not move_found:
                print('Oops.. This is not a valid move. Does it capture as much as possible?')
                continue

            move_found = move_found[0]
            return move_found, move_str

    def requestCoordinate(msg):
        str = input(msg)
        return ConsoleView.coordinateToIndex(str)

    def coordinateToIndex(str):
        line_idx = str[0]
        col_idx = int(str[1])
        
        line_idx = ConsoleView.LETTERS.index(line_idx)
        col_idx -= 1

        return (line_idx, col_idx)
    
    def indexToCoordinate(i, j):
        line_coord = ConsoleView.LETTERS[i]
        col_coord = j + 1

        return line_coord + str(col_coord)