import random

class TokenPool:
    def __init__(self,tokenlist=None,red=0,green=0,blue=0,black=0,white=0):
        if tokenlist!=None:
            self.red = tokenlist[0]
            self.green = tokenlist[1]
            self.blue = tokenlist[2]
            self.black = tokenlist[3]
            self.white = tokenlist[4]
        else:
            self.red = red
            self.green = green
            self.blue = blue
            self.black = black
            self.white = white

    def asList(self):
        return [self.red,self.green,self.blue,self.black,self.white]

    def __add__(self,other):
        if type(other) == type(self):
            self.red += other.red
            self.green += other.green
            self.blue += other.blue
            self.black += other.black
            self.white += other.white
        else:
            raise TypeError("cannot add by types other than tokenpool")

    def __sub__(self,other):
        if type(other) == type(self):
            self.red -= other.red
            self.green -= other.green
            self.blue -= other.blue
            self.black -= other.black
            self.white -= other.white
        else:
            raise TypeError("cannot subtract by types other than tokenpool")

    def __lt__(self,other):
        if type(other) != type(self):
            raise TypeError("comparation error")
        else:
            return (self.red < other.red) and (self.green < other.green) \
                   and (self.blue < other.blue) and (self.black < other.black) \
                   and (self.white < other.white)

    def __eq__(self,other):
        if type(other) != type(self):
            raise TypeError("comparation error")
        else:
            return (self.red==other.red) and (self.blue==other.blue) \
                   and (self.green==other.green) and (self.black==other.black) \
                   and (self.white==other.white)

class CardData:
    def __init__(self,costdata,victory_points,gembonus_string):
        self.victory_points = victory_points
        self.cost = costdata
        self.gembonus = gembonus_string

    def gembonus_asid(self):
        return ["red","green","blue","black","white"].index(self.gembonus)

    def gembonus_astokenpool(self):
        s = [0]*5
        t = self.gembonus_asid()
        s[t] = 1
        return TokenPool(s)

class Card:
    def __init__(self,carddata,isfacedown=False):
        self.carddata=carddata
        self.isfacedown = isfacedown

    def tofaceup(self):
        self.isfacedown = False

    def tofacedown(self):
        self.isfacedown = True

    def flip(self):
        self.isfacedown = not self.isfacedown

class Noble:
    def __init__(self,victory_points,cost):
        self.victory_points = victory_points
        self.cost = cost

    def isplayergetting(player):
        return cost < player.passive_tokens or cost == player.passive_tokens

class Player:
    def __init__(self,name=""):
        self.name = name

        self.active_tokens = TokenPool()
        self.passive_tokens = TokenPool()
        self.joker_tokens = 0

        self.cards_onhold = []

        self.cards_bought = []

        self.nobles = []

    def setname(name):
        self.name = name

    def add_tokens(self,tokenpool):
        self.active_tokens += tokenpool

    def add_tokens_to_passive(self,card):
        self.passive_tokens += card.gembonus_astokenpool()

    def add_joker(self,joker):
        self.joker += joker

    def add_nobles(self,noble):
        self.nobles.append(noble)

    def hold_card(self,card):
        self.cards_onhold.append(card)

    def pay_joker(self,joker):
        self.joker -= joker

    def remove_tokens(self,tokenpool):
        self.active_tokens -= tokenpool

    def release_hold_card(self,index):
        c = self.card_onhold.pop(index)
        return c

    def total_victory_points(self):
        s = 0
        for noble in self.nobles:
            s += noble.victory_points
        for card in cards_bought:
            s += card.victory_points
        return s

class Deck:
    """
    Deck is a pile of cards with ordered arrangement.

    attributes:
        deck: list of cards in the deck with 0 is the index of the top card.
    """
    def __init__(self,cards=None):
        """construct a Deck object with container containing Card objects as .deck"""
        if cards != None:
            self.deck = list(cards)
        else:
            self.deck = []
        
    def cards_in_deck(self):
        return len(self.deck)
    
    def add_card_totop(self,card):
        """add a card to the top of the deck, equivalent to insert_card(0,card)"""
        self.deck.insert(0,card)

    def add_card_tobottom(self,card):
        """add a card to the bottom of the deck"""
        self.deck.append(card)

    def add_cards_totop(self,cards):
        """add a pile of cards to the top of the deck"""
        self.deck = self.deck + list(cards)

    def add_cards_tobottom(self,cards):
        """add a pile of cards to the bottom of the deck"""
        self.deck = list(cards) + self.deck
        
    def insert_card(self,index,card):
        """insert a card to the deck, similar to list.insert"""
        self.deck.insert(index,card)

    def insert_card_random(self,card):
        """insert a card into a random place in the deck"""
        self.deck.insert(random.randint(0,len(self.deck)),card)
        
    def top_card(self):
        """returns the top card of the deck"""
        try:
            return self.deck[0]
        except:
            raise ValueError("top_card error") 
    
    def draw_card(self):
        """removes the top card from the deck and returns it"""
        try:
            card_drawn = self.deck.pop(0)
            return card_drawn
        except:
            raise ValueError("draw_card error")
        
    def shuffle(self):
        """shuffles the cards in the deck using random.shuffle"""
        random.shuffle(self.deck)
