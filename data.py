from objects import Player
from board import Board

#Class game data
class SetData():
    i=0
    isRunning = True
    #listRender.append((Surface,positon)) only
    listRender = []

    players = []
    for i in range(4):
        players.append(Player())

    board = Board()

    def update(self):
        self.i+=1
        if self.i == 60:
            print("Thick!")
            self.i=0
        
gamedata = SetData()
