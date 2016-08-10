import pygame
from data import gamedata
from button import Button
from gameplay import GamePlay

pygame.font.init()
BG_IMG = 'asset/menu/bg.png'
START_IMG = 'asset/menu/start-button.png'
HTP_IMG = 'asset/menu/htp-button.png'
EXIT_IMG = 'asset/menu/exit-button.png'
FONT_HEADER = pygame.font.Font(None, 72)
FONT_NORMAL = pygame.font.Font(None, 36)

class Menu():
    def __init__(self):
        self.bg = pygame.image.load(BG_IMG)
        self.header = FONT_HEADER.render('Splendor',1,(200,200,0))
        
        self.bStartgame = Button(pygame.image.load(START_IMG),(550,200))
        self.bHowtoplay = Button(pygame.image.load(HTP_IMG),(550,300))
        self.bExit = Button(pygame.image.load(EXIT_IMG),(550,400))
        
        self.toggleExit = False
        self.exitHeader = FONT_HEADER.render('EXIT',1,(20,20,20))
        self.exitText = FONT_NORMAL.render('Are you sure?',1,(20,20,20))
        self.bYes = Button(FONT_NORMAL.render('Yes',1,(20,20,20)),(560,280))
        self.bNo = Button(FONT_NORMAL.render('No',1,(20,20,20)),(680,280))

    def update(self):
        gamedata.listRender.append((self.bg,(0,0)))
        gamedata.listRender.append((self.header,(100,50)))
                          
        if self.toggleExit:
            gamedata.listRender.append((self.exitHeader,(530,180)))
            gamedata.listRender.append((self.exitText,(550,230)))
            self.bYes.render()
            self.bNo.render()
        else:
            self.bStartgame.render()
            self.bHowtoplay.render()
            self.bExit.render()

        if self.bStartgame.isclicked():
            gamedata.state = 'gameplay'
            gamedata.gameplay = GamePlay()
                          
        if self.bExit.isclicked():
            self.toggleExit = True

        if self.bNo.isclicked():
            self.toggleExit = False

        if self.bYes.isclicked():
            gamedata.isRunning = False
            pygame.quit()
