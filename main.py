import pygame, sys
from pygame.locals import *
from classes import *

pygame.init()
clock = pygame.time.Clock()
#BLOCKS = list()
# for x in range(SIZE*SIZE):
#     BLOCKS.append(Block([x % SIZE == 0, x % SIZE == SIZE-1, x // SIZE == 0, x // SIZE == SIZE - 1]))
# MAZE = Maze(BLOCKS, SIZE)

MAZE = MazeCreation().create_random_maze()


#MAZE = Maze((Block((True,False,True,False)),), 1)
DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 20))

pygame.display.set_caption("Maze")

while True:
    DISPLAYSURF.fill((255, 255, 255))

    DISPLAYSURF.blit(MAZE.surface, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            MAZE.update_wall(event.pos)
    pygame.display.update()
    clock.tick(60)
