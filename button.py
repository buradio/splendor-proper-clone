import pygame
from data import gamedata
#class button for imprement
class Button():
    def __init__(self,surface,position=(0,0)):
        self.surface = surface
        self.position = position
        self.height = surface.get_height()
        self.width = surface.get_width()
    #function in button
    def ispressed(self):
        if self.ishovered() and gamedata.isPressing:
            print("pressed")
            return True
        return False
        
    def isclicked(self):
        if self.ishovered() and gamedata.isClicking:
            print("clicked")
            return True
        return False

    def ishovered(self):
        mousepos = pygame.mouse.get_pos()
        if self.position[0]<=mousepos[0]<=self.position[0]+self.width and\
           self.position[1]<=mousepos[1]<=self.position[1]+self.height:
            #print("hovered")
            return True
        return False

    def render(self):
        gamedata.listRender.append((self.surface,self.position))
        
