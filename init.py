from consoleView import ConsoleView

def main():
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
    ConsoleView.requestMovement()
    


if __name__ == '__main__':
    main()