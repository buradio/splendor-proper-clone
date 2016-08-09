import pygame
from objects import Player
from board import Board

#Class game data
class SetData():
    def __init__(self):
        self.isRunning = True

        self.isPressing = False
        self.isClicking = False
        
        #listRender.append((Surface,positon)) only
        self.listRender = []

        self.players = []
        for i in range(4):
            self.players.append(Player())

        self.board = Board()
        
gamedata = SetData()
