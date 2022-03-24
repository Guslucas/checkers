from pickle import NONE
import global_vars
from pieces.piece import Piece

class PieceChange:

    def movePiece(current_turn, movement_coord):
        from_coord, to_coord = movement_coord
        from_i, from_j = from_coord
        to_i, to_j = to_coord
        #Transforma o conteudo da coordenada origem para a de destino
        global_vars.matrix[to_i][to_j] = global_vars.matrix[from_i][from_j]
        #Transforma o conteudo da coordenada origem em None
        global_vars.matrix[from_i][from_j] = None

        #Printa o conteudo da coordenada origem 
        #print(global_vars.matrix[from_coord[0]][from_coord[1]])