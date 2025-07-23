import pygame
pygame.init
screen = pygame.display.set_mode((1000,1000))

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.circle(screen,(0,255,0),(500,500),50)
    pygame.draw.circle(screen,(0,255,0),(50,500),50,10)
    pygame.display.flip()