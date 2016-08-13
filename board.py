from objects import *
import random

def load_deck(filename):
    infile = open(filename)
    a = []
    for line in infile:
        l = line.split(",")[1:]
        g = l[0]
        pv = int(l[1])
        tp = TokenPool([int(i) for i in l[2:]])
        c = CardData(tp,pv,g)
        card = Card(c)
        a.append(card)

    return a

def load_nobles(nobles_list):
    f = open(nobles_list)
    a = []
    for line in f:
        l = [int(i) for i in line.split(",")]
        pv = l[0]
        c = l[1:]
        tp = TokenPool(c)
        noble = Noble(pv,tp)
        a.append(noble)

    return a


class Board:
    def __init__(self):
        self.deck1 = Deck(load_deck("cardslist/level1.csv"))
        self.deck1.shuffle()
        self.deck2 = Deck(load_deck("cardslist/level2.csv"))
        self.deck2.shuffle()
        self.deck3 = Deck(load_deck("cardslist/level3.csv"))
        self.deck3.shuffle()

        self.tier1 = []
        for i in range(4):
            self.tier1.append(self.deck1.draw_card())
        self.tier2 = []
        for i in range(4):
            self.tier2.append(self.deck2.draw_card())
        self.tier3 = []
        for i in range(4):
            self.tier3.append(self.deck3.draw_card())

        self.tokenpool = TokenPool([7,7,7,7,7])

        self.joker = 5
        noble_list = load_nobles("cardslist/nobles.csv")
        self.nobles = random.sample(noble_list,5)
