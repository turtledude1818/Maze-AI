from enum import Enum
import pygame

length = 40

class Walls(Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3
class WallPosition(Enum):
    LEFT = ((0, 0), (0, length))
    RIGHT = ((length, length), (length, 0))
    TOP = ((length, 0), (0, 0))
    BOTTOM = ((0, length), (length, length))

class Block():
    def __init__(self, walls):
        self.walls = walls
        self.surface = pygame.Surface((length, length))
        self.surface.fill((255, 255, 255))
        self.draw()

    def get_wall(self, location):
        if location == Walls.LEFT.value:
            return WallPosition.LEFT
        if location == Walls.RIGHT.value:
            return WallPosition.RIGHT
        if location == Walls.TOP.value:
            return WallPosition.TOP
        return WallPosition.BOTTOM

    def draw(self):
        self.surface.fill((255, 255, 255))
        for location, wall in enumerate(self.walls):
            if wall:
                points = self.get_wall(location).value
                pygame.draw.line(self.surface, (0, 0, 0), points[0], points[1], 5)

    def get_surf(self):
        return self.surface

class Maze():
    def __init__(self, blocks, size):
        self.blocks = blocks
        self.size = size
        self.surface = pygame.Surface((size*40, size*40))
        self.draw()
    def draw(self):
        for position, block in enumerate(self.blocks):
            self.surface.blit(block.get_surf(), ((position % self.size) * 40, (position // self.size) * 40))
