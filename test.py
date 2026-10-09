import pygame

pygame.init()

#global variables for width and height!
WINDOW_WIDTH = 640 
WINDOW_HEIGHT = 480
screen = pygame.display.set_mode((640, 480)) 

#x positions for stars 1 and 2!
stars1x = 0
stars2x = 640

#rainbow sprites/ animation!
class player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
         super()._init_()
         self.sprites = []
         self.sprites.append(pygame.image.load('rainbow 1.png'))
         self.sprites.append(pygame.image.load('rainbow 2.png'))
         self.sprites.append(pygame.image.load('rainbow 3.png'))
         self.sprites.append(pygame.image.load('rainbow 4.png'))
         self.sprites.append(pygame.image.load('rainbow 5.png'))
         self.sprites.append(pygame.image.load('rainbow 6.png'))
         self.current_sprite = 0
         self.image = self.sprites[self.current_sprite]
         
         self.rect = self.image.get_rect()
         self.rect.topleft = [pos_x,pos_y]
                             
#loading images! 
gamebackground1 = pygame.image.load("game bg 1.png").convert() 
stars_1 = pygame.image.load("game stars.png").convert_alpha()
stars_2 = pygame.image.load("game stars.png").convert_alpha()
clouds = pygame.image.load("game clouds.png").convert_alpha()
boarder = pygame.image.load("game boarders.png").convert_alpha()
pipi = pygame.image.load("game pipi.png").convert_alpha()
rainbow1 = pygame.image.load("rainbow 1.png").convert_alpha()
rainbow2 = pygame.image.load("rainbow 2.png").convert_alpha()
rainbow3 = pygame.image.load("rainbow 3.png").convert_alpha()
rainbow4 = pygame.image.load("rainbow 4.png").convert_alpha()
rainbow5 = pygame.image.load("rainbow 5.png").convert_alpha()
rainbow6 = pygame.image.load("rainbow 6.png").convert_alpha()

running = True 
clock = pygame.time.Clock()

#game loop!
while running: 
    
    screen.blit(gamebackground1, (0,0))
    screen.blit(stars_1, (stars1x,0))
    screen.blit(stars_2, (stars2x, 0))
    screen.blit(clouds, (0,0))
    screen.blit(boarder, (0,0))
    screen.blit(pipi, (0,0))
    
    stars1x -= 3
    stars2x -= 3
    
    #star animation loop
    if stars1x <= -WINDOW_WIDTH:
        stars1x = WINDOW_WIDTH
        
    if stars2x <= -WINDOW_WIDTH:
        stars2x = WINDOW_WIDTH
        
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    pygame.display.flip()
    
    clock.tick(60)
            
pygame.quit()
#SAVE IT PLEASE BEFORE RUNNING!!!!!