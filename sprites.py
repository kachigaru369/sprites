import pygame , sys

class Crosshair(pygame.sprite.Sprite):
    def __init__(self,width , height ,pos_x ,pos_y ,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x , pos_y]
#general setup
pygame.init()
clock = pygame.time.Clock()

#game screen 
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width , screen_height))
background = pygame.image.load("")

crosshair = Crosshair(50,50 ,100,100 , ("white"))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.flip()
    screen.blit(background,(0,0))
    crosshair_group.draw(screen)
    clock.tick(60)
