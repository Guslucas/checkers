import os
from shutil import move
from turtle import pos
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
    is_cpu = False

    while True:
        ConsoleView.showCheckers()
        possibleMoves = possibleMovesCalculator.getPossibleMoves(turnManager.turn)
        if not possibleMoves:
            turnManager.swapTurn()
            print('GAME OVER. ', turnManager.currentTeam(), ' wins!')
            break
        if show_answers:
            print(possibleMoves)
        move, move_str = ConsoleView.requestValidMove(possibleMoves, turnManager, is_cpu)
        print(move)
        MoveApplier.apply(move, move_str, turnManager.turn, show_every_move, is_cpu)

        turnManager.swapTurn()
        print('TURN IS NOW ', turnManager.turn)

if __name__ == '__main__':
    main()