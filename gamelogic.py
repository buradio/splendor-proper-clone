from data import gamedata
from objects import *

#gamelogic

class Gamelogic:

    def __init__(self):
        self.currentturn = 0
        self.isending = False
        gamedata.players[0].isplaying = True

    def shiftturn(self):
        #check for nobles
        self.check_for_nobles(gamedata.board.nobles,gamedata.players[self.currentturn])
        #advance turn order
        gamedata.players[self.currentturn].isplaying = False
        self.currentturn += 1
        if self.currentturn == len(gamedata.players):
            self.currentturn = 0
        gamedata.players[self.currentturn].isplaying = True

        #check if any player has got 15 points
        if gamedata.players[self.currentturn].total_victory_points() >= 15:
            self.isending = True

        if self.isending and self.currentturn == len(gamedata.players)-1:
            #end game
            pass

    def player_buy_card(self,player,deck,tierlist,index):
        cost = tierlist[index].carddata.cost

        #subtract by passive tokens
        cost -= player.passive_tokens
        cost = TokenPool([max(0,i) for i in cost.asList()])


        if player.active_tokens > cost:
            #buy card
            player.active_tokens -= cost
            card = tierlist[index]
            tierlist[index] = deck.draw_card()
            player.cards_bought.append(card)
            print("card bought!")
            #shiftturn
            self.shiftturn()
        else:
            #fail buy
            print("failed to buy card")

    def player_buy_hold_card(self,player,index):
        cost = player.cards_onhold[index]

        #subtract by passive tokens
        cost -= player.passive_tokens
        cost = TokenPool([max(0,i) for i in cost.asList()])

        #check if can buy
        if player.active_tokens > cost or player.activetokens.asList() > cost.asList():
            #buy card
            player.active_tokens -= cost
            player.cards_bought.append(player.cards_onhold[index])
            player.cards_onhold[index] = None
            self.shiftturn()
        else:
            #buy fail
            print("buy hold card failed")
            pass


    def check_for_nobles(self,nobles,player):
        if len(player.nobles) == 0:
            for noble in nobles:
                if noble.isplayergetting(player):
                    #move noble to player
                    if player.nobles == []:
                        player.nobles.append(noble)

    def player_convert_joker(self,player,colorid):
        if player.joker_tokens>0:
            player.joker_tokens -= 1
            temp_list = player.active_tokens.asList()
            temp_list[colorid] += 1

            player.active_tokens = TokenPool(temp_list)

        else:
            print("convert joker failed")

    def player_take_three(self,colorids,player):
        take_list = [1 if i in colorids else 0 for i in range(5)]
        take_pool = TokenPool(take_list)
        gamedata.board.tokenpool -= take_pool
        player.active_tokens += take_pool
        #shift turn
        self.shiftturn()

    def player_take_two(self,colorid,player):
        take_list = [2 if i in colorid else 0 for i in range(5)]
        take_pool = TokenPool(take_list)
        gamedata.board.tokenpool -= take_pool
        player.active_tokens += take_pool
        self.shiftturn()

    def player_take_card(self,board,tierlist,deck,index,player):
        card = tierlist[index]
        tierlist[index] = None
        player.cards_onhold.append(card)
        #add joker token if possible
        if board.joker > 0:
            board.joker -= 1
            player.joker_tokens += 1
        #open a new card for card taken
        tierlist[index] = deck.draw_card()
        self.shiftturn()
