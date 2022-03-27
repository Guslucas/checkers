import os
from shutil import move
from turtle import pos
from pieceChange import PieceChange
import global_vars
from pieces.piece import Piece
from pieces.king import King
from consoleView import ConsoleView
from possibleMovesCalculator import PossibleMovesCalculator
from turnManager import TurnManager
from moveApplier import MoveApplier

def initBoard():
    matrix = [
        [0, 1, 0, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 1, 0, 1, 0], 
        [0, 1, 0, 1, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [2, 0, 2, 0, 2, 0, 2, 0], 
        [0, 2, 0, 2, 0, 2, 0, 2], 
        [2, 0, 2, 0, 2, 0, 2, 0],
    ]

    # Test scenarios

    # matrix = [
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 1, 0, 0, 0, 0, 0], 
    #     [0, 2, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    # matrix = [
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 1, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 1, 0, 0, 0, 2, 0], 
    #     [0, 2, 0, 0, 0, 0, 0, 2], 
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    # matrix = [
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 1, 0, 1, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 1, 0, 1, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 1, 0, 0, 0, 2, 0], 
    #     [0, 2, 0, 0, 0, 0, 0, 2], 
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    # same, but diff color
    # matrix = [
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 0, 2, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 2, 0, 2, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 2, 0, 2, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    # matrix = [
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 1, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 2, 0, 0, 0, 0, 0],
    # ]
    # # other team
    # matrix = [
    #     [0, 0, 0, 0, 0, 1, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 2, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    # matrix = [
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 1, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 2, 0, 0, 0, 0, 0],
    # ]
    # other team
    # matrix = [
    #     [0, 0, 0, 0, 0, 1, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 2, 0, 2, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 2, 0, 2, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 2, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    

    matrix = [[Piece('w') if el == 2 else (Piece('b') if el == 1 else None) for el in x] for x in matrix]
    # matrix[7][2].promote_to_king()
    # matrix[0][5].promote_to_king()
    return matrix

def main():
    global_vars.matrix = initBoard()
    possibleMovesCalculator = PossibleMovesCalculator()


    turnManager = TurnManager('w')
    show_answers = False
    show_every_move = True
    is_cpu = True

    while True:
        ConsoleView.showCheckers()
        possibleMoves = possibleMovesCalculator.getPossibleMoves(turnManager.turn)
        if not possibleMoves:
            print('GAME OVER. ', turnManager.swapTurn(), ' wins!')
            break
        if show_answers:
            print(possibleMoves)
        move, move_str = ConsoleView.requestValidMove(possibleMoves, turnManager.turn, is_cpu)
        print(move)
        MoveApplier.apply(move, move_str, turnManager.turn, show_every_move, is_cpu)

        turnManager.swapTurn()
        print('TURN IS NOW ', turnManager.turn)

    #ConsoleView.showCheckers()
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