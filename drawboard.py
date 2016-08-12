from data import gamedata
from objects import *
from board import Board
import pygame

pygame.init()

#constants
#card_on_board
CARD_ON_BOARD_SIZE = (90, 120)
CARD_ON_BOARD_VICTORY_POINTS_FONT = pygame.font.Font(None, 36)
CARD_COST_FONT = pygame.font.Font(None, 15)
CARD_COST_ICONS = ["asset/icon/token-red.png",
                   "asset/icon/token-green.png",
                   "asset/icon/token-blue.png",
                   "asset/icon/token-black.png",
                   "asset/icon/token-white.png"]
CARD_GEMBONUS_ICONS = ["asset/icon/token-red-big.png",
                       "asset/icon/token-green-big.png",
                       "asset/icon/token-blue-big.png",
                       "asset/icon/token-black-big.png",
                       "asset/icon/token-white-big.png"]
CARD_ON_BOARD_VICTORY_POINTS_COLOR = (0,0,0)
COST_TEXT_COLOR = (255,255,255)
CARD_COST_SIZE = (25,10)
CARD_COST_ICON_SIZE = (10,10)

#deck
DECK_SIZE = (90, 120)
DECK_NUMBER_OF_CARDS_FONT = pygame.font.Font(None,30)
DECK_NUMBER_OF_CARDS_POS = (15,90)
DECK_NUMBER_OF_CARDS_TEXT_COLOR = (0,0,0)
DECK_TIER1_BACK = "asset/card-back/tier1-back.png"
DECK_TIER2_BACK = "asset/card-back/tier2-back.png"
DECK_TIER3_BACK = "asset/card-back/tier3-back.png"

#board_token_pool
BOARD_TOKEN_ICONS = ["asset/board/token-red.png",
                     "asset/board/token-green.png",
                     "asset/board/token-blue.png",
                     "asset/board/token-black.png",
                     "asset/board/token-white.png"]
BOARD_JOKER_ICON = "asset/board/token-joker.png"
BOARD_TOKENPOOL_SIZE = (560,75)
BOARD_TOKENPOOL_ICON_SIZE = (75,75)
BOARD_TOKENPOOL_FONT = pygame.font.Font(None,30)
BOARD_TOKENPOOL_TEXT_POS = (60,60)
BOARD_TOKENPOOL_TEXT_COLOR = (255,0,0)

#playerpanel
PLAYERPANEL_BG_IMAGE = "asset/board/playerpanel-back.png"
PLAYERPANEL_SIZE = (200,150)
PLAYERPANEL_NAME_FONT = pygame.font.Font(None,26)
PLAYERPANEL_CARD_SIZE = (40,40)
PLAYERPANEL_NAME_COLOR = (255,255,255)
PLAYERPANEL_ICONS = ["asset/icon/token-red.png",
                   "asset/icon/token-green.png",
                   "asset/icon/token-blue.png",
                   "asset/icon/token-black.png",
                   "asset/icon/token-white.png"]
PLAYERPANEL_ICON_SIZE = (20,20)
PLAYERPANEL_TOKEN_FONT = pygame.font.Font(None, 26)
PLAYERPANEL_TOKEN_TEXT_ACTIVE_COLOR = (255,255,255)
PLAYERPANEL_TOKEN_TEXT_PASSIVE_COLOR = (150,150,150)
PLAYERPANEL_JOKER_ICON_SIZE = (20,20)
PLAYERPANEL_JOKER_ICON = "asset/icon/token-joker.png"
PLAYERPANEL_PV_ICON_SIZE = (20,20)
PLAYERPANEL_PV_ICON = "asset/board/playerpanel-vp-icon.png"

#board
BOARD_SIZE = (800,600)
BOARD_BG_IMAGE = "asset/board/board-bg.png"

def draw_card_on_board(card):
    surface = pygame.Surface(CARD_ON_BOARD_SIZE)

    #draw faceart
    faceart = pygame.image.load(card.faceart)
    surface.blit(faceart,(0,0))

    #draw victory points
    if card.carddata.victory_points != 0:
        victory_points = card.carddata.victory_points
        vp_text = str(victory_points)
        vp_font = CARD_ON_BOARD_VICTORY_POINTS_FONT
        vp_render = vp_font.render(vp_text,1,CARD_ON_BOARD_VICTORY_POINTS_COLOR)
        surface.blit(vp_render,(60,45))

    #draw gembonus
    #to be implemented
    gembonus_surf = pygame.Surface((30,30))
    gembonus_icon_id = card.carddata.gembonus_asid()
    gembonus_icon = pygame.image.load(CARD_GEMBONUS_ICONS[gembonus_icon_id])
    gembonus_surf.blit(gembonus_icon,(0,0))
    surface.blit(gembonus_surf,(55,5))

    #draw costs
    costs = card.carddata.cost.asList()
    draw_list = []
    #color: r,g,b,k,w
    for i in range(5):
        if costs[i]!=0:
            temp_surf = pygame.Surface(CARD_COST_SIZE)

            #draw icon
            icon_surf = pygame.Surface(CARD_COST_ICON_SIZE)
            icon_img = pygame.image.load(CARD_COST_ICONS[i])
            icon_surf.blit(icon_img,(0,0))

            #draw cost text
            cost_text = str(costs[i])
            cost_font = CARD_COST_FONT
            cost_render = cost_font.render(cost_text,1,COST_TEXT_COLOR)

            temp_surf.blit(icon_surf, (0,0))
            temp_surf.blit(cost_render, (15,0))

            draw_list.append(temp_surf)

    y = 5
    for surf in draw_list:
        surface.blit(surf,(5,y))
        y+=15


    return surface

def draw_deck(deck,backart="asset/card-back/tier1-back.png"):
    surface = pygame.Surface(DECK_SIZE)

    #draw backart
    backart_img = pygame.image.load(backart)
    surface.blit(backart_img,(0,0))

    #draw number of cards
    numcard = deck.cards_in_deck()
    numcard_text = str(numcard)
    numcard_font = DECK_NUMBER_OF_CARDS_FONT
    numcard_render = numcard_font.render(numcard_text,1,DECK_NUMBER_OF_CARDS_TEXT_COLOR)
    surface.blit(numcard_render, DECK_NUMBER_OF_CARDS_POS)
    return surface

def draw_board_token_icon(colorid,number):
    #token_icon_surf = pygame.Surface(BOARD_TOKENPOOL_ICON_SIZE)
    #draw token icon
    token_icon_surf = pygame.image.load(BOARD_TOKEN_ICONS[colorid])
    #token_icon_surf.fill((255,0,255))
    #token_icon_surf.blit(token_icon_img,(0,0))

    #draw token number
    token_num_surf = pygame.Surface((20,20))
    token_num_text = str(number)
    token_num_font = BOARD_TOKENPOOL_FONT
    token_num_render = token_num_font.render(token_num_text,1,BOARD_TOKENPOOL_TEXT_COLOR)
    token_num_surf.blit(token_num_render,(0,0))
    token_icon_surf.blit(token_num_surf,BOARD_TOKENPOOL_TEXT_POS)
    return token_icon_surf

def draw_board_joker_icon(joker):
    joker_icon_surf = pygame.Surface(BOARD_TOKENPOOL_ICON_SIZE, pygame.SRCALPHA, 32)
    joker_icon_surf=joker_icon_surf.convert_alpha()
    #draw joker icon
    joker_icon_img = pygame.image.load(BOARD_JOKER_ICON)
    #joker_icon_surf.fill((255,0,255))
    joker_icon_surf.blit(joker_icon_img,(0,0))

    #draw joker number
    joker_num_surf = pygame.Surface((20,20))
    joker_num_text = str(joker)
    joker_num_font = BOARD_TOKENPOOL_FONT
    joker_num_render = joker_num_font.render(joker_num_text,1,BOARD_TOKENPOOL_TEXT_COLOR)
    joker_num_surf.blit(joker_num_render,(0,0))
    joker_icon_surf.blit(joker_num_surf,BOARD_TOKENPOOL_TEXT_POS)

    return joker_icon_surf

def draw_board_token_pool(tokenpool,joker):
    token_list = tokenpool.asList()
    pool_surface = pygame.Surface(BOARD_TOKENPOOL_SIZE, pygame.SRCALPHA, 32)
    #pool_surface.fill((255,0,255))
    pool_surface=pool_surface.convert_alpha()
    x = 0
    for i in range(5):
        token_surf = draw_board_token_icon(i,token_list[i])
        pool_surface.blit(token_surf,(x,0))
        x+=97

    joker_surf = draw_board_joker_icon(joker)
    pool_surface.blit(joker_surf,(x,0))
    #pool_surface.set_colorkey((255,0,255))

    return pool_surface

def draw_noble(noble):
    #to be implemented
    surface = pygame.Surface((75,75))
    surface.fill((0,222,222))
    return surface

def draw_player_panel(player):
    playerpanel_surface = pygame.Surface(PLAYERPANEL_SIZE)
    playerpanel_back_image = pygame.image.load(PLAYERPANEL_BG_IMAGE)
    playerpanel_surface.blit(playerpanel_back_image,(0,0))

    #draw cards on hold
    y = 5
    for card in player.cards_onhold:
        temp_surf = pygame.Surface(PLAYERPANEL_CARD_SIZE)
        #to be implemented
        temp_surf.fill((0,200,200))

        playerpanel_surface.blit(temp_surf,(0,y))

        y += 50

    #draw player name
    name_font = PLAYERPANEL_NAME_FONT
    name_render = name_font.render(player.name,1,PLAYERPANEL_NAME_COLOR)
    playerpanel_surface.blit(name_render,(60,16))
    #draw marker is playing
    if player.isplaying:
        #may be change style later
        selector_surf = pygame.Surface((10,10))
        selector_surf.fill((255,240,45))
        playerpanel_surface.blit(selector_surf,(60+name_render.get_width()+10,20))

    x = 60
    for i in range(5):
        #draw token icons
        icon_surf = pygame.Surface(PLAYERPANEL_ICON_SIZE)
        icon_img = pygame.image.load(PLAYERPANEL_ICONS[i])
        icon_surf.blit(icon_img,(0,0))

        #draw active token number
        anum_surf = pygame.Surface(PLAYERPANEL_ICON_SIZE)
        anum_surf.fill((0,0,0))
        anum_text = str(player.active_tokens.asList()[i])
        anum_font = PLAYERPANEL_TOKEN_FONT
        anum_render = anum_font.render(anum_text,1,
                                       PLAYERPANEL_TOKEN_TEXT_ACTIVE_COLOR)
        anum_surf.blit(anum_render,(0,0))

        #draw passive token number
        pnum_surf = pygame.Surface(PLAYERPANEL_ICON_SIZE)
        pnum_surf.fill((0,0,0))
        pnum_text = str(player.passive_tokens.asList()[i])
        pnum_font = PLAYERPANEL_TOKEN_FONT
        pnum_render = pnum_font.render(pnum_text,1,
                                       PLAYERPANEL_TOKEN_TEXT_PASSIVE_COLOR)
        pnum_surf.blit(pnum_render,(0,0))

        #blits
        playerpanel_surface.blit(icon_surf,(x,45))
        playerpanel_surface.blit(anum_surf,(x,70))
        playerpanel_surface.blit(pnum_surf,(x,95))

        x += 25

    #draw joker token icon
    jicon_surf = pygame.Surface(PLAYERPANEL_JOKER_ICON_SIZE)
    jicon_img = pygame.image.load(PLAYERPANEL_JOKER_ICON)
    jicon_surf.blit(jicon_img,(0,0))

    playerpanel_surface.blit(jicon_surf,(60,125))
    #draw joker token number
    jnum_surf = pygame.Surface(PLAYERPANEL_ICON_SIZE)
    jnum_surf.fill((0,0,0))
    jnum_text = str(player.joker_tokens)
    jnum_font = PLAYERPANEL_TOKEN_FONT
    jnum_render = jnum_font.render(jnum_text,1,
                                   PLAYERPANEL_TOKEN_TEXT_ACTIVE_COLOR)
    jnum_surf.blit(jnum_render,(0,0))
    playerpanel_surface.blit(jnum_surf,(85,125))

    #draw victory points icon
    pvicon_surf = pygame.Surface(PLAYERPANEL_PV_ICON_SIZE)
    pvicon_img = pygame.image.load(PLAYERPANEL_PV_ICON)
    pvicon_surf.blit(pvicon_img,(0,0))

    playerpanel_surface.blit(pvicon_surf,(135,125))
    #draw victory points number
    pvnum_surf = pygame.Surface(PLAYERPANEL_ICON_SIZE)
    pvnum_surf.fill((0,0,0))
    pvnum_text = str(player.total_victory_points())
    pvnum_font = PLAYERPANEL_TOKEN_FONT
    pvnum_render = pvnum_font.render(pvnum_text,1,
                                   PLAYERPANEL_TOKEN_TEXT_ACTIVE_COLOR)
    pvnum_surf.blit(pvnum_render,(0,0))
    playerpanel_surface.blit(pvnum_surf,(160,125))

    return playerpanel_surface

def draw_board(board,players):
    #create board surface
    board_surface = pygame.Surface(BOARD_SIZE)
    board_bg = pygame.image.load(BOARD_BG_IMAGE)
    board_surface.blit(board_bg,(0,0))

    #draw nobles
    x = 20

    for i in range(5):
        temp_surf = draw_noble(None)
        board_surface.blit(temp_surf,(x,20))
        x += 75+37

    #draw deck1
    deck1_surf = draw_deck(board.deck1,DECK_TIER1_BACK)
    board_surface.blit(deck1_surf,(20,110))
    #draw tier1
    x = 171
    for card in board.tier1:
        card_surf = draw_card_on_board(card)
        board_surface.blit(card_surf,(x,110))
        x+=90+11

    #draw deck2
    deck2_surf = draw_deck(board.deck2,DECK_TIER2_BACK)
    board_surface.blit(deck2_surf,(20,240))
    #draw tier2
    x = 171
    for card in board.tier2:
        card_surf = draw_card_on_board(card)
        board_surface.blit(card_surf,(x,240))
        x+=90+11

    #draw deck3
    deck3_surf = draw_deck(board.deck3,DECK_TIER3_BACK)
    board_surface.blit(deck3_surf,(20,370))
    #draw tier3
    x = 171
    for card in board.tier3:
        card_surf = draw_card_on_board(card)
        board_surface.blit(card_surf,(x,370))
        x+=90+11

    #draw tokenpool
    tkp_surf = draw_board_token_pool(board.tokenpool,board.joker)
    board_surface.blit(tkp_surf,(20,505))

    #draw players
    y=0
    for player in players:
        pl_surf = draw_player_panel(player)
        board_surface.blit(pl_surf,(600,y))
        y+=150

    return board_surface

class DrawBoardData():
    def __init__(self):
        self.nobles = None
        self.deck1 = None
        self.tier1 = None
        self.tier2 = None
        self.tier3 = None

        #boardbg
        self.boardbg = pygame.image.load(BOARD_BG_IMAGE)

    def update(self,board,players):
        #add .nobles
        x = 20
        self.nobles = []
        for i in range(5):
            temp_surf = draw_noble(None)
            self.nobles.append((temp_surf,(x,20)))
            x += 75+37

        #add .deck1
        deck1_surf = draw_deck(board.deck1,DECK_TIER1_BACK)
        self.deck1 = (deck1_surf,(20,110))

        #add .tier1
        x = 171
        self.tier1 = []
        for card in board.tier1:
            card_surf = draw_card_on_board(card)
            self.tier1.append((card_surf,(x,110)))
            x+=90+11

        #add .deck2
        deck2_surf = draw_deck(board.deck2,DECK_TIER2_BACK)
        self.deck2 = (deck2_surf,(20,240))

        #add .tier2
        x = 171
        self.tier2 = []
        for card in board.tier2:
            card_surf = draw_card_on_board(card)
            self.tier2.append((card_surf,(x,240)))
            x+=90+11

        #add .deck3
        deck3_surf = draw_deck(board.deck3,DECK_TIER3_BACK)
        self.deck3 = (deck3_surf,(20,370))

        #add .tier3
        x = 171
        self.tier3 = []
        for card in board.tier3:
            card_surf = draw_card_on_board(card)
            self.tier2.append((card_surf,(x,370)))
            x+=90+11

        #add .tokenpool
        self.tokenpool = []
        x = 20
        for i in range(5):
            token_icon_surf = draw_board_token_icon(i,board.tokenpool.asList()[i])
            self.tokenpool.append((token_icon_surf,(x,505)))
            x+=97

        #add .joker
        joker_surf = draw_board_joker_icon(board.joker)
        self.joker = (joker_surf,(505,505))

        #add .players
        y=0
        self.players = []
        for player in players:
            pl_surf = draw_player_panel(player)
            self.players.append((pl_surf,(600,y)))
            y+=150




#testing: create window to blit
if __name__ == "__main__":
    s = pygame.display.set_mode((850,650))
    gamedata.board = Board()
    gamedata.players[2].isplaying=True
    board_surf = draw_board(gamedata.board,gamedata.players)
    s.blit(board_surf,(0,0))
    pygame.display.flip()
