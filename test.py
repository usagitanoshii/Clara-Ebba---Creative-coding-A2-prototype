import pygame

pygame.init()


#global variables for width and height!
WINDOW_WIDTH = 640 
WINDOW_HEIGHT = 480
screen = pygame.display.set_mode((640, 480)) 


#x positions for stars 1 and 2!
stars1x = 0
stars2x = 640

#create explosion class
class Explosion(pygame.sprite.Sprite): 
    def __init__(self, pos): 
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 17):
            img = pygame.image.load(f"img/frame_{num}.png")
            img = pygame.transform.scale(img, (90,90))
            self.images.append(img)
        self.index = 0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos 
        self.counter = 0 
        
    def update(self):
        explosion_speed = 4 
        #update explosion animation 
        self.counter += 1
        
        if self.counter >= explosion_speed and self.index <len(self.images) - 1: 
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
            
        #if animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

explosion_group = pygame.sprite.Group() 

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
class Window(pygame.sprite.Sprite): 
    def __init__(self,pos_x,pos_y):
             super().__init__()
             self.sprites = [] 
             self.sprites.append(pygame.image.load('window 1.png'))
             self.sprites.append(pygame.image.load('fish window 1.png'))
             self.sprites.append(pygame.image.load('fish window 2.png'))
             self.sprites.append(pygame.image.load('fish window 3.png'))
             self.sprites.append(pygame.image.load('fish window 4.png'))
             self.current_sprite = 0 
             self.image = self.sprites[self.current_sprite]
             
             self.rect = self.image.get_rect()
             self.rect.topleft = [pos_x,pos_y]
             
    def update(self):
        self.current_sprite += 0.15
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        print(f"current sprite {self.current_sprite}")
        
        self.image = self.sprites[int(self.current_sprite)]    

            
#creating the sprites and the groups (window 2)!
closed_window = Window(0,0)
window1 = Window(105,115)
window2 = Window(-99,115)
window3 = Window(0,115)
window4 = Window(105,0)
window5 = Window(-99,0) 
moving_sprites.add(closed_window)                                                               
moving_sprites.add(window1)
moving_sprites.add(window2)
moving_sprites.add(window3)
moving_sprites.add(window4)
moving_sprites.add(window5)

#cross hair controls
rows, cols = (2,3)

cross_pos = [[0 for i in range(cols)] for j in range(rows)]
cross_pos[0][0] = (-99,0)
cross_pos[1][0] = (-99,115)
cross_pos[0][1] = (0,0)
cross_pos[1][1] = (0,115) 
cross_pos[0][2] = (105,0)
cross_pos[1][2] = (105,115)

row = 1
col = 1

#loading images! 
gamebackground1 = pygame.image.load("game bg 1.png").convert() 
stars_1 = pygame.image.load("game stars.png").convert_alpha()
stars_2 = pygame.image.load("game stars.png").convert_alpha()
clouds = pygame.image.load("game clouds.png").convert_alpha()
boarder = pygame.image.load("game boarders.png").convert_alpha()
pipi = pygame.image.load("game pipi.png").convert_alpha()
cloud_cart = pygame.image.load("cloud cart.png").convert_alpha()
cross_hair = pygame.image.load("cross hair.png").convert_alpha()

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
    screen.blit(cross_hair, cross_pos[row][col])          
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if col != 0:
                col -= 1
        
        if keys[pygame.K_UP]:
            if row != 0:
                row -= 1
            
        if keys[pygame.K_RIGHT]:
            if col != 2:
                col += 1
            
        if keys[pygame.K_DOWN]:
            if row != 1:
                row += 1
                
        if keys[pygame.K_SPACE]:
            explosion = Explosion(cross_pos[row][col])
            explosion_group.add(explosion)          
         
     #draw background (explosion)
    explosion_group.draw(screen)
    explosion_group.update()           

    pygame.display.flip()
        
    moving_sprites.update()    
    
    clock.tick(60)
            
pygame.quit()
#SAVE IT PLEASE BEFORE RUNNING!!!!!