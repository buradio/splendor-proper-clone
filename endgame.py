import pygame
from data import gamedata

class EndGame():
    def __init__(self):
        self.bg = pygame.image.load('/asset/endgame/bg.png')
    def update(self):
        gamedata.listRender.append((self.bg,(0,0)))
