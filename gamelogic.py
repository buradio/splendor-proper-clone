from data import gamedata

#gamelogic

class Gamelogic:
    
    def init(self,data):
        self.currentturn = 0
        self.data = gamedata
        self.isending = False

    def shiftturn(self):
        #advance turn order
        self.currentturn += 1
        if self.currentturn == len(gamedata.players):
            self.currentturn = 0

        #check if any player has got 15 points
        if gamedata.players[self.currentturn].total_victory_points >= 15:
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
        else:
            #try to buy with joker
            pass
            #fail buy
            pass

    def check_for_nobles(self,nobles,player):
        for noble in nobles:
            if noble.isplayergetting(player):
                #move noble to player
                if player.nobles == []:
                    player.nobles.append(noble)
                break

    def player_take_three(self,colorids,player):
        take_list = [1 if i in colorids else 0 for i in range(5)]
        take_pool = TokenPool(take_list)
        gamedata.board.tokenpool -= take_pool
        player.active_tokens += take_pool

    def player_take_two(self,colorid,player):
        take_list = [2 if i==colorid else 0 for i in range(5)]
        take_pool = TokenPool(take_list)
        gamedata.board.tokenpool -= take_pool
        player.active_tokens += take_pool

    def player_take_card(self,tierlist,deck,index,player):
        card = tierlist[index]
        tierlist[index] = None
        player.cards_onhold.append(card)
        #open a new card for card taken
        tierlist[index] = deck.draw_card()
        pass
        
