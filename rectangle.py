import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(0,0,255),pygame.Rect(30,30,60,60))
    pygame.draw.rect(screen,(0,0,255),pygame.Rect(100,100,60,60),5)
    pygame.display.flip()


