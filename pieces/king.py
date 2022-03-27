import global_vars
from placeOnBoardValidation import PlaceOnBoardValidation
from consoleView import ConsoleView
from coordinateTranslator import CoordinateTranslator
from pieces.piece import Piece

class King(Piece):

    SYMBOLS = [' ♚ ', ' ♔ ']

    def __init__(self, color):
        pass
    
    
    def update_symbol(self):
        self.symbol = King.SYMBOLS[self.ALLOWED_COLORS.index(self.color)]

    def maxCapturingMoves(self, i, j, turn):
        coord = ConsoleView.indexToCoordinate(i, j)
        return self.recMaxCapturingMove(i, j, turn, coord, 0, global_vars.matrix, True)
    
    def recMaxCapturingMove(self, i, j, turn, current_route, current_capture, matrix, first_time = False):
        isOffBoard = not PlaceOnBoardValidation.isOnBoard((i, j))
        if isOffBoard:
            return None
        
        directions_capitalization = []
        for direction in CoordinateTranslator.DIRECTIONS:
            
            enemy_i = None
            enemy_j = None

            # walk until see a piece
            steps = 1
            while True:
                can_move = self.place_moving(i, j, turn, direction, steps, matrix)

                place_at_board, new_i, new_j = can_move
                
                # out of the board
                if place_at_board == False:
                    break
                
                if place_at_board is not None:
                    if place_at_board.color != turn:
                        # if it's not an enemy, don't try to capture it
                        enemy_i = new_i
                        enemy_j = new_j
                    break
                
                # only consider walking if it hasn't captured yet
                if first_time:
                    directions_capitalization.append(([current_route + ConsoleView.indexToCoordinate(new_i, new_j)], 0))
                
                steps += 1
                
            # If saw an enemy, search for other or end of board, to calculate possible movement
            if enemy_i:
                other_i = enemy_i
                other_j = enemy_j
                steps = 1
                while True:
                    can_move = self.place_moving(other_i, other_j, turn, direction, steps, matrix)

                    place_at_board, new_i, new_j = can_move
                    
                    
                    # out of the board Or found a barrier, stop
                    if place_at_board == False or place_at_board is not None:
                        break
                    
                    print('Could capture to ', new_i, new_j)

                    new_matrix = [row[:] for row in matrix]
                    new_matrix[new_i][new_j] = new_matrix[i][j]
                    new_matrix[enemy_i][enemy_j] = None
                    new_matrix[i][j] = None

                    capture_moves = self.recMaxCapturingMove(new_i, new_j, turn, current_route + ConsoleView.indexToCoordinate(new_i, new_j), current_capture + 1, new_matrix)
                    if capture_moves is None:
                        directions_capitalization.append(([current_route + ConsoleView.indexToCoordinate(new_i, new_j)], current_capture + 1))
                    else:
                        directions_capitalization.append(capture_moves)
                    
                    steps += 1

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

    
    def place_moving(self, i, j, turn, direction, steps, matrix):
        coord_dir = CoordinateTranslator(turn, i, j, matrix)
        coord_dir.moveDiag(steps, direction)

        # can move
        return coord_dir.placeAtBoard(), coord_dir.i, coord_dir.j