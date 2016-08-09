import pygame
from objects import Player
from board import Board

#Class game data
class SetData():
    i=0
    isRunning = True

    isPressing = False
    isClicking = False
    
    #listRender.append((Surface,positon)) only
    listRender = []

    players = []
    for i in range(4):
        players.append(Player())

    board = Board()
        
gamedata = SetData()
