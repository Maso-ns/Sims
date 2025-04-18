import pygame, sys
import numpy as np

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Placeholder")

while True:
    if pygame.event.peek(pygame.QUIT) or pygame.event.peek(pygame.K_ESCAPE):
        pygame.quit()
        sys.exit()