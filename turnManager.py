class TurnManager:
    def __init__(self, turn = 'w'):
        self.turn = turn

    def swapTurn(self):
        if self.turn == 'w':
            self.turn = 'b'        
        else:
            self.turn = 'w'
        return self.turn
    
    def currentTeam(self):
        if self.turn == 'w':
            return 'White team'
        return 'Black team'