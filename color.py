import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock() 

done = False

try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        for i in range(0, 59):
            j = 0
            for j in range(0, 59):
                color = (random.randint(0,200), random.randint(0,200), random.randint(0,200))
                pygame.draw.rect(screen, color, (10*(j)+5,10*(i)+5,10,10), 2)
    
        pygame.display.flip()
        clock.tick(30) # framerate
except:
    print('Yielded error.')
