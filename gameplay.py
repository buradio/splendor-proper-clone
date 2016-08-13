import pygame
from drawboard import*
from data import gamedata
from board import Board
from button import Button
from gamelogic import Gamelogic

class GamePlay():
    def __init__(self):
        gamedata.board = Board()
        self.board_surf = DrawBoardData()
        self.gamelg = Gamelogic()
        self.selected_token = []

    def update(self):

        #update board and set button
        self.board_surf.update(gamedata.board,gamedata.players)
        self.bnoble = [Button(noble[0],noble[1]) for noble in self.board_surf.nobles]
        self.bdeck1 = Button(self.board_surf.deck1[0],self.board_surf.deck1[1])
        self.btier1 = [Button(card[0],card[1]) for card in self.board_surf.tier1]
        self.bdeck2 = Button(self.board_surf.deck2[0],self.board_surf.deck2[1])
        self.btier2 = [Button(card[0],card[1]) for card in self.board_surf.tier2]
        self.bdeck3 = Button(self.board_surf.deck3[0],self.board_surf.deck3[1])
        self.btier3 = [Button(card[0],card[1]) for card in self.board_surf.tier3]
        self.btokenpool = [Button(token[0],token[1]) for token in self.board_surf.tokenpool]
        self.bjoker = Button(self.board_surf.joker[0],self.board_surf.joker[1])
        for player in gamedata.players:
            if player.isplaying:
                self.player = player

        #click and hover function
        for bnoble in self.bnoble:
            if bnoble.isclicked():
                self.gamelg.shiftturn()
        if self.bdeck1.ishovered():
            print("deck1 is hovered")
        for btier1 in self.btier1:
            if btier1.isclicked():
                pass
        if self.bdeck2.ishovered():
            print("deck2 is hovered")
        for btier2 in self.btier2:
            if btier2.isclicked():
                pass
        if self.bdeck3.ishovered():
            print("deck3 is hovered")
        for btier3 in self.btier3:
            if btier3.isclicked():
                pass
        for btoken in range(len(self.btokenpool)):
            if self.btokenpool[btoken].isclicked():
                if not(len(self.selected_token) == 2 and btoken in self.selected_token):
                    if gamedata.board.tokenpool.asList()[btoken] > 0:
                        self.selected_token.append(btoken)
                if self.selected_token.count(btoken) == 2 and len(self.selected_token) == 2:
                    if gamedata.board.tokenpool.asList()[btoken] > 3:
                        self.gamelg.player_take_two(self.selected_token,self.player)
                        self.selected_token = []
                    else:
                        self.selected_token.pop()
                if len(self.selected_token) == 3:
                    self.gamelg.player_take_three(self.selected_token,self.player)
                    self.selected_token = []
        if self.bjoker.isclicked():
            pass

        #render
        gamedata.listRender.append((self.board_surf.boardbg,(0,0)))
        gamedata.listRender.append(self.board_surf.deck1)
        gamedata.listRender.append(self.board_surf.deck2)
        gamedata.listRender.append(self.board_surf.deck3)
        for player in self.board_surf.players:
            gamedata.listRender.append(player)
        for bnoble in self.bnoble:
            bnoble.render()
        for btier1 in self.btier1:
            btier1.render()
        for btier2 in self.btier2:
            btier2.render()
        for btier3 in self.btier3:
            btier3.render()
        for btoken in self.btokenpool:
            btoken.render()
        self.bjoker.render()
