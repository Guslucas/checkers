import global_vars
from consoleView import ConsoleView
from coordinateTranslator import CoordinateTranslator
from placeOnBoardValidation import PlaceOnBoardValidation
class Piece:
    ALLOWED_COLORS = ['b', 'w']
    SYMBOLS = ' ○ ', ' ● '

    def __init__(self, color):
        if color not in self.ALLOWED_COLORS:
            raise ValueError(f"Invalid color {color}.")
        self.color = color
        self.symbol = Piece.SYMBOLS[0 if color == 'b' else 1]
        self.max_capturing_route = ''
    
    def __repr__(self):
        return self.symbol
    
    def maxCapturingMoves(self, i, j, turn):
        coord = ConsoleView.indexToCoordinate(i, j)
        max_capturing_move = self.recMaxCapturingMove(i, j, turn, coord, 0, global_vars.matrix)
        
        if max_capturing_move is None:
            directions_to_move = []
            for direction in CoordinateTranslator.TOP_DIRECTIONS:
                can_move = self.canMove(i, j, turn, direction, global_vars.matrix)
                if (can_move):
                    move_i, move_j = can_move
                    directions_to_move.append(coord + ConsoleView.indexToCoordinate(move_i, move_j))
            return (directions_to_move, 0)

        return max_capturing_move

    def recMaxCapturingMove(self, i, j, turn, current_route, current_capture, matrix, last_direction = None):
        isOffBoard = not PlaceOnBoardValidation.isOnBoard((i, j))
        if isOffBoard:
            return None
        
        directions_capitalization = []
        
        directions_to_consider = CoordinateTranslator.DIRECTIONS
        
        if last_direction:
            directions_to_consider = CoordinateTranslator.DIRECTIONS.copy()
            
            disregard_last_direction = last_direction.copy()
            disregard_last_direction['i'] *= -1
            disregard_last_direction['j'] *= -1

            directions_to_consider.remove(disregard_last_direction)
        
        for direction in directions_to_consider:
            can_capture = self.canCapture(i, j, turn, direction, matrix)

            if can_capture:
                di, dj = direction.values()
                
                el = CoordinateTranslator(turn, i, j, matrix)
                el.i += di
                el.j += dj
                el.translateIfNeeded()

                el2 = CoordinateTranslator(turn, i, j, matrix)
                el2.i += di*2
                el2.j += dj*2
                el2.translateIfNeeded()
                
                new_matrix = [row[:] for row in matrix]
                new_matrix[el2.i][el2.j] = new_matrix[i][j]
                new_matrix[el.i][el.j] = None
                new_matrix[i][j] = None

                capture_moves = self.recMaxCapturingMove(el2.i, el2.j, turn, current_route + ConsoleView.indexToCoordinate(el2.i, el2.j), current_capture + 1, new_matrix, direction)
                if capture_moves is None:
                    directions_capitalization.append(([current_route + ConsoleView.indexToCoordinate(el2.i, el2.j)], current_capture + 1))
                else:
                    directions_capitalization.append(capture_moves)

        # if cant capture in any directions, return current
        if not directions_capitalization:
            return None

        # if can capture in any direction, get the directions with most captures
        max_capturing_count = max(directions_capitalization, key = lambda i : i[1])[1]
        capturing_routes_list = list(map(lambda el: el[0], filter(lambda el: el[1] == max_capturing_count, directions_capitalization)))
        
        flattened_capturing_routes_list = []
        for el in capturing_routes_list:
            flattened_capturing_routes_list.extend(el)

        return (flattened_capturing_routes_list, max_capturing_count)

    def canCapture(self, i, j, turn, direction, matrix):
        coord_dir = CoordinateTranslator(turn, i, j, matrix)
        coord_dir_2 = CoordinateTranslator(turn, i, j, matrix)
        coord_dir.moveDiag(1, direction)
        coord_dir_2.moveDiag(2, direction)
        
        place_dir = coord_dir.placeAtBoard()
        return (place_dir is not None and place_dir != False and place_dir.color != turn) and coord_dir_2.placeAtBoard() is None
    
    def canMove(self, i, j, turn, direction, matrix):
        coord_dir = CoordinateTranslator(turn, i, j, matrix)
        coord_dir.moveDiag(1, direction)

        # can move
        if (coord_dir.placeAtBoard() is None):
            return coord_dir.i, coord_dir.j
        return False

    def promote_to_king(self):
        from pieces.king import King
        self.__class__ = King
        self.update_symbol()
            