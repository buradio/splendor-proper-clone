import pygame
from data import gamedata
from control import*
from button import Button
from menu import Menu
from gameplay import GamePlay

class SetGame():
    
    #constants
    DISPLAY_SIZE = DISPLAY_WIDTH,DISPLAY_HEIGHT = 800,600
    FPS = 60
    TITLE = "SPLENDOR"
    
    def __init__(self):
        pygame.init()
        #screen and display
        self.screen = pygame.display.set_mode(self.DISPLAY_SIZE)
        pygame.display.set_caption(self.TITLE)
        #clock thick
        self.clock = pygame.time.Clock()
        #create menu
        gamedata.state = 'menu'
        gamedata.menu = Menu()
        
    def loop(self):
        gamedata.isRunning = True
        while gamedata.isRunning:
            self.clock.tick(self.FPS)
            #input phase
            self.inputFunc()
            if gamedata.isRunning:
                #logic phase
                statemanagement()
                if gamedata.isRunning:
                    #render phase
                    self.render()
                    gamedata.isClicking = False

    def inputFunc(self):
        #input event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    leftclickDown()
                if event.button == 3:
                    rightclickDown()
            if event.type == pygame.MOUSEBUTTONUP:
                #print(event.button)
                if event.button == 1:
                    leftclickUp()
                if event.button == 3:
                    rightclickUp()
            if event.type == pygame.MOUSEMOTION:
                #print(event.pos)
                pass
            if event.type == pygame.KEYDOWN:
                #print(pygame.key.name(event.key))
                keydDown(event.key)
            if event.type == pygame.KEYUP:
                #print(pygame.key.name(event.key))
                keyUp(event.key)
    
    def render(self):
        for i in range(len(gamedata.listRender)):
            self.screen.blit(gamedata.listRender[i][0],gamedata.listRender[i][1])
        pygame.display.flip()
        gamedata.listRender = []
        
    def quit(self):
        gamedata.isRunning = False
        pygame.quit()
        
def statemanagement():
    if gamedata.state == 'menu':
        gamedata.menu.update()
    elif gamedata.state == 'gameplay':
        gamedata.gameplay.update()

#initialize game
game = SetGame()
#call gameloop
game.loop()
