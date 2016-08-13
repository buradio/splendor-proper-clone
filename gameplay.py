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
        self.selected_joker = False

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
                pass

        if self.bdeck1.ishovered():
            print("deck1 is hovered")
        for card in range(len(self.btier1)):
            if self.btier1[card].isclicked():
                print('tier1 '+str(card))
                if self.selected_joker:
                    self.gamelg.player_take_card(gamedata.board,gamedata.board.tier1,gamedata.board.deck1,card,self.player)
                    self.selected_joker = False
                else:
                    self.gamelg.player_buy_card(self.player,gamedata.board.deck1,gamedata.board.tier1,card)
        if self.bdeck2.ishovered():
            print("deck2 is hovered")
        for card in range(len(self.btier2)):
            if self.btier2[card].isclicked():
                print('tier2 '+str(card))
                if self.selected_joker:
                    self.gamelg.player_take_card(gamedata.board,gamedata.board.tier2,gamedata.board.deck2,card,self.player)
                    self.selected_joker = False
                else:
                    self.gamelg.player_buy_card(self.player,gamedata.board.deck2,gamedata.board.tier2,card)
        if self.bdeck3.ishovered():
            print("deck3 is hovered")
        for card in range(len(self.btier3)):
            if self.btier3[card].isclicked():
                print('tier3 '+str(card))
                if self.selected_joker:
                    self.gamelg.player_take_card(gamedata.board,gamedata.board.tier3,gamedata.board.deck3,card,self.player)
                    self.selected_joker = False
                else:
                    self.gamelg.player_buy_card(self.player,gamedata.board.deck3,gamedata.board.tier3,card)

        #click token
        for btoken in range(len(self.btokenpool)):
            if self.btokenpool[btoken].isclicked():
                if not(len(self.selected_token) == 2 and btoken in self.selected_token) and not(self.selected_joker):
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
            if self.btokenpool[btoken].isRclicked():
                if btoken in self.selected_token:
                    self.selected_token.remove(btoken)
        #click joker
        if self.bjoker.isclicked():
            if self.selected_token == []:
                self.selected_joker = True
        if self.bjoker.isRclicked():
            self.selected_joker = False

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
        for btoken in range(len(self.btokenpool)):
            if btoken in self.selected_token:
                self.btokenpool[btoken].renderselected()
            else:
                self.btokenpool[btoken].render()
        if self.selected_joker:
            self.bjoker.renderselected()
        else:
            self.bjoker.render()
