import pygame

pygame.init()
WINDOW_WIDTH = 640 
WINDOW_HEIGHT = 480
screen = pygame.display.set_mode((640, 480)) 

gamebackground1 = pygame.image.load("game bg 1.png").convert()

running = True 
while running: 
    
    screen.blit(gamebackground1, (0,0))
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    pygame.display.flip()
            
pygame.quit()
