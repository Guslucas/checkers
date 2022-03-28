import global_vars

class PossibleMovesCalculator:
    def getPossibleMoves(self , turn):

        maxCapturePiece = 0
        piecesCapturing = []

        pieces = [(i, j, item) for i, sublist in enumerate(global_vars.matrix) for j, item in enumerate(sublist) if item is not None and item.color == turn]
        

        for pieceStructure in pieces:
            i, j, piece = pieceStructure
            
            (routes, captured) = piece.maxCapturingMoves(i, j, turn)
            if not routes:
                continue
            if captured < maxCapturePiece:
                continue
            
            if captured > maxCapturePiece:
                maxCapturePiece = captured
                piecesCapturing = []
            
            # >=
            piecesCapturing.append((routes, i, j, piece))

        return piecesCapturing