import pygame
from objects import Player

#Class game data
class SetData():
    def __init__(self):
        self.isRunning = True

        self.isPressing = False
        self.isClicking = False
        self.isRClicking = False

        #listRender.append((Surface,positon)) only
        self.listRender = []

        self.players = []
        for i in range(4):
            self.players.append(Player("player" + str(i)))

        self.board = None

        self.gameplay = None

gamedata = SetData()
