import os
from turtle import pos
from pieceChange import PieceChange
import global_vars
from pieces.piece import Piece
from pieces.king import King
from consoleView import ConsoleView
from possibleMovesCalculator import PossibleMovesCalculator
from turnManager import TurnManager

def initBoard():
    # matrix = [
    #     [0, 1, 0, 1, 0, 1, 0, 1], 
    #     [1, 0, 1, 0, 1, 0, 1, 0], 
    #     [0, 1, 0, 1, 0, 2, 0, 1], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [2, 0, 2, 0, 2, 0, 1, 0], 
    #     [0, 2, 0, 2, 0, 2, 0, 2], 
    #     [2, 0, 2, 0, 2, 0, 2, 0],
    # ]

    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0, 1, 0], 
        [0, 2, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    

    matrix = [[Piece('w') if el == 2 else (Piece('b') if el == 1 else None) for el in x] for x in matrix]

    return matrix

def main():
    global_vars.matrix = initBoard()
    possibleMovesCalculator = PossibleMovesCalculator()

    # TODO turn manager
    
    turnManager = TurnManager()
    
    ConsoleView.showCheckers()
    possibleMoves = possibleMovesCalculator.getPossibleMoves(turnManager.turn)
    
    # movement_coord = ConsoleView.requestMovement(turn)

    # if movement_coord not in possibleMoves:
    #     return None

    # #print(movement_coord)
    # PieceChange.movePiece(turn, movement_coord)

    # turn = 'b'
    # # For testing clear console
    # ConsoleView.showCheckers()
    # movement_coord = ConsoleView.requestMovement(turn)
    # #print(movement_coord)
    # PieceChange.movePiece(turn, movement_coord)
    
    # ConsoleView.showCheckers()
    
    # p = Piece('b')
    # k = King('b')
    # print(f"{type(p)}")
    # print(f"{type(k)}")
    # print(f"{isinstance(p, King)}")
    # print(f"{isinstance(k, King)}")


    #p = Piece('b')
    #k = King('b')
    #print(f"{type(p)}")
    #print(f"{type(k)}")
    #print(f"{isinstance(p, King)}")
    #print(f"{isinstance(k, King)}")

if __name__ == '__main__':
    main()