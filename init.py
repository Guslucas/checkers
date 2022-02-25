import os
from consoleView import ConsoleView

def main():
    print(os.system("chcp"))
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
    
    ConsoleView.showCheckers(matrix)
    print(ConsoleView.requestMovement())

    # For testing clear console
    ConsoleView.showCheckers(matrix)
    print(ConsoleView.requestMovement())
    


if __name__ == '__main__':
    main()