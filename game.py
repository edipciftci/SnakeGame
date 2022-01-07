# Create a snake game using pygame

# Import necessary modules

import pygame
import random
import time

# Create game window

width = 1080
height = 720

pygame.init()
window = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()