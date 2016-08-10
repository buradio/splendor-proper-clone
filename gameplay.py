import pygame
from data import gamedata

class GamePlay():
    def __init__(self):
        self.bg = pygame.image.load('asset/gameplay/bg.png')
    def update(self):
        gamedata.listRender.append((self.bg,(0,0)))
