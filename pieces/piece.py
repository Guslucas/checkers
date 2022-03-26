import re
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
        max_capturing_move = self.recMaxCapturingMove(i, j, turn, coord)
        
        if max_capturing_move is None:
            directions_to_move = []
            for direction in CoordinateTranslator.TOP_DIRECTIONS:
                if (self.canMove(i, j, turn, direction)):
                    directions_to_move.append(coord + ConsoleView.indexToCoordinate(i + direction['i'], j + direction['j']))
            return (directions_to_move, 0)

        return max_capturing_move

    def recMaxCapturingMove(self, i, j, turn, current_route, current_capture = 0):
        isOffBoard = not PlaceOnBoardValidation.isOnBoard((i, j))
        if isOffBoard:
            return None
        
        directions_capitalization = {}
        for direction in CoordinateTranslator.DIRECTIONS:
            can_capture = self.canCapture(i, j, turn, direction)

            if can_capture:
                di, dj = direction.values()
                capture_moves = self.recMaxCapturingMove(i + di*2, j + dj*2, turn, current_route + ConsoleView.indexToCoordinate(i + di*2, j + dj*2), current_capture + 1)
                if capture_moves is None:
                    directions_capitalization[direction.values()] = ([current_route + ConsoleView.indexToCoordinate(i + di*2, j + dj*2)], current_capture + 1)
                else:
                    directions_capitalization[direction.values()] = capture_moves

        # if cant capture in any directions, return current
        if not directions_capitalization:
            return None

        # if can capture in any direction, get the directions with most captures
        max_capturing_value = max(directions_capitalization.values(), key = lambda i : i[1])[1]
        #max_capturing_direction = dict(filter(lambda el: el[1][1] == 1, directions_capitalization.items()))
        capturing_routes_list = list(map(lambda el: el[0], filter(lambda el: el[1] == max_capturing_value, directions_capitalization.values())))
        capture_count = list(directions_capitalization.values())[0][1]

        return (capturing_routes_list, capture_count)

    def canCapture(self, i, j, turn, direction):
        coord_dir = CoordinateTranslator(turn, i, j)
        coord_dir_2 = CoordinateTranslator(turn, i, j)
        coord_dir.moveDiag(1, direction)
        coord_dir_2.moveDiag(2, direction)
        
        place_dir = coord_dir.placeAtBoard()
        return (place_dir and place_dir.color != turn) and coord_dir_2.placeAtBoard() is None
    
    def canMove(self, i, j, turn, direction):
        coord_dir = CoordinateTranslator(turn, i, j)
        coord_dir.moveDiag(1, direction)
        return not coord_dir.placeAtBoard() 

            