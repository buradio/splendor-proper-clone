import pygame
from data import gamedata

def leftclickDown():
    gamedata.isPressing = True

def rightclickDown():
    pass

def leftclickUp():
    gamedata.isPressing = False
    gamedata.isClicking = True

def rightclickUp():
    gamedata.isRClicking = True

def keydDown(key):
    if key == pygame.K_s:
        gamedata.isRunning = False

def keyUp(key):
    pass
