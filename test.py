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
class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
         super().__init__()
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
         
    def update(self):
        self.current_sprite += 0.2
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        print(f"current sprite {self.current_sprite}")  
        
        self.image = self.sprites[int(self.current_sprite)]
                   
#creating the sprites and groups (rainbow)! 
moving_sprites = pygame.sprite.Group()
player = Player (0,-6)
moving_sprites.add(player)          

#window sprites/ animation! 
class Window(pygame.sprtite.Sprite): 
    def __init__(self,pos_x,pos_y):
             super().__init__()
             self.sprites = [] 
             self.sprites.append(pygame.image.load('window 1.png'))
             self.sprites.append(pygame.image.load('window 2.png'))
             self.sprites.append(pygame.image.load('window 3.png'))
             self.sprites.append(pygame.image.load('window 4.png'))
             self.sprites.append(pygame.image.load('window 5.png'))
             
    def update(self):
        self.current_sprite += 0.2
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        print(f"current sprite {self.current_sprite}")
        
        self.image = self.sprites[int(self.current_sprite)]    
            
#creating the sprites and the groups (window)!
moving_sprites = pygame.sprite.Group()
window = Window (0,0)
moving_sprites.add(window)                                                                

#loading images! 
gamebackground1 = pygame.image.load("game bg 1.png").convert() 
stars_1 = pygame.image.load("game stars.png").convert_alpha()
stars_2 = pygame.image.load("game stars.png").convert_alpha()
clouds = pygame.image.load("game clouds.png").convert_alpha()
boarder = pygame.image.load("game boarders.png").convert_alpha()
pipi = pygame.image.load("game pipi.png").convert_alpha()
cloud_cart = pygame.image.load("cloud cart.png").convert_alpha()

running = True 
clock = pygame.time.Clock()

#game loop!
while running: 
    
    screen.blit(gamebackground1, (0,0))
    screen.blit(stars_1, (stars1x,0))
    screen.blit(stars_2, (stars2x, 0))
    screen.blit(cloud_cart, (0,0))
    screen.blit(clouds, (0,0))
    screen.blit(boarder, (0,0))
    moving_sprites.draw(screen)

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
        
    moving_sprites.update()    
    
    clock.tick(60)
            
pygame.quit()
#SAVE IT PLEASE BEFORE RUNNING!!!!!