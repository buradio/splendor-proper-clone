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
            print("clicked"+str(self.position))
            return True
        return False

    def isRclicked(self):
        if self.ishovered() and gamedata.isRClicking:
            return True
        return False

    def ishovered(self):
        mousepos = pygame.mouse.get_pos()
        if self.position[0]<=mousepos[0]<=self.position[0]+self.width and\
           self.position[1]<=mousepos[1]<=self.position[1]+self.height:
            #print("hovered"+str(self.position))
            return True
        return False

    def render(self):
        gamedata.listRender.append((self.surface,self.position))

    def renderselected(self):
        temp_S = pygame.Surface((10,10))
        temp_S.fill((255,0,255))
        self.surface.blit(temp_S,(self.width//2-5,self.height//2-5))
        self.render()
