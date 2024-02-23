""" pyGame tutorial """

import pygame


pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
    