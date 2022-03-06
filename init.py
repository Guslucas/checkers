import os
import global_vars
from consoleView import ConsoleView

def main():
    print(os.system("chcp"))
    global_vars.matrix = [
                [0, 1, 0, 1, 0, 1, 0, 1], 
                [1, 0, 1, 0, 1, 0, 1, 0], 
                [0, 1, 0, 1, 0, 1, 0, 1], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0], 
                [2, 0, 2, 0, 2, 0, 2, 0], 
                [0, 2, 0, 2, 0, 2, 0, 2], 
                [2, 0, 2, 0, 2, 0, 2, 0], 
            ]
    matrix = global_vars.matrix

    # TODO turn manager
    turn = 2
    ConsoleView.showCheckers()
    print(ConsoleView.requestMovement(turn))

    turn = 1
    # For testing clear console
    ConsoleView.showCheckers()
    print(ConsoleView.requestMovement(turn))
    


if __name__ == '__main__':
    main()