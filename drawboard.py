from data import gamedata
from objects import *
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

                     

def draw_card_on_board(card):
    surface = pygame.Surface(CARD_ON_BOARD_SIZE)

    #draw faceart
    faceart = pygame.image.load(card.faceart)
    surface.blit(faceart,(0,0))

    #draw victory points
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

def draw_board_token_pool(tokenpool,joker):
    token_list = tokenpool.asList()
    pool_surface = pygame.Surface(BOARD_TOKENPOOL_SIZE)
    x = 0
    for i in range(5):
        #draw token icon
        token_icon_img = pygame.image.load(BOARD_TOKEN_ICONS[i])
        token_icon_surf = pygame.Surface(BOARD_TOKENPOOL_ICON_SIZE)
        token_icon_surf.blit(token_icon_img,(0,0))

        #draw token number
        token_num_surf = pygame.Surface((20,20))
        token_num_text = str(token_list[i])
        token_num_font = BOARD_TOKENPOOL_FONT
        token_num_render = token_num_font.render(token_num_text,1,BOARD_TOKENPOOL_TEXT_COLOR)
        token_num_surf.blit(token_num_render,(0,0))
        token_icon_surf.blit(token_num_surf,BOARD_TOKENPOOL_TEXT_POS)

        pool_surface.blit(token_icon_surf,(x,0))
        x+=97

    #draw joker
    #draw joker icon
    joker_icon_img = pygame.image.load(BOARD_JOKER_ICON)
    joker_icon_surf = pygame.Surface(BOARD_TOKENPOOL_ICON_SIZE)
    joker_icon_surf.blit(joker_icon_img,(0,0))
    
    #draw joker number
    joker_num_surf = pygame.Surface((20,20))
    joker_num_text = str(joker)
    joker_num_font = BOARD_TOKENPOOL_FONT
    joker_num_render = token_num_font.render(joker_num_text,1,BOARD_TOKENPOOL_TEXT_COLOR)
    joker_num_surf.blit(joker_num_render,(0,0))
    joker_icon_surf.blit(joker_num_surf,BOARD_TOKENPOOL_TEXT_POS)

    pool_surface.blit(joker_icon_surf,(x,0))

    return pool_surface

#testing: create window to blit
test_card = Card(CardData(TokenPool([5,1,0,2,4]) ,5,"green"))
surface = draw_card_on_board(test_card)
s = pygame.display.set_mode((800,800))
s.blit(surface,(15,15))

surface2 = draw_deck(Deck())
s.blit(surface2,(145,15))

surface22 = draw_deck(Deck(),"asset/card-back/tier2-back.png")
s.blit(surface22,(245,15))

surface22 = draw_deck(Deck(),"asset/card-back/tier3-back.png")
s.blit(surface22,(345,15))

surface3 = draw_board_token_pool(TokenPool([1,5,4,2,7]),5)
s.blit(surface3,(15,150))
pygame.display.flip()
