import pygame, sys
from pygame.locals import *
from classes import *

pygame.init()
clock = pygame.time.Clock()
SIZE = 20
BLOCKS = list()
for x in range(SIZE*SIZE):
    BLOCKS.append(Block((x % SIZE == 0, x % SIZE == SIZE-1, x // SIZE == 0, x // SIZE == SIZE - 1)))
MAZE = Maze(BLOCKS, SIZE)

#MAZE = Maze((Block((True,False,True,False)),), 1)
DISPLAYSURF = pygame.display.set_mode((800, 800))
#DISPLAYSURF = pygame.display.set_mode((MAZE.size*length, MAZE.size*length))

pygame.display.set_caption("Maze")
while True:
    DISPLAYSURF.fill((255, 255, 255))

    DISPLAYSURF.blit(MAZE.surface, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
