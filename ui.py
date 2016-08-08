
# Function create surface

def getImg(fileName):
    try:
        return pygame.image.load('asset/image/'+fileName)
    except NameError:
        print("can't find "+'asset/image/'+fileName)
        errorImg = pygame.Surface((50,50))
        errorImg.fill((250,0,0))
        return errorImg

def getText(text,size=16,font=None,color=(0,0,0)):
    Font = pygame.font.Font(font,size)
    return Font.render(text,1,color)
