from enum import Enum
import pygame

SIZE = 5
WINDOW_SIZE = 800
LENGTH = WINDOW_SIZE // SIZE

class Walls(Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3

class WallPosition(Enum):
    LEFT = ((0, 0), (0, LENGTH))
    RIGHT = ((LENGTH, LENGTH), (LENGTH, 0))
    TOP = ((LENGTH, 0), (0, 0))
    BOTTOM = ((0, LENGTH), (LENGTH, LENGTH))

class Block():
    def __init__(self, walls):
        self.walls = walls
        self.surface = pygame.Surface((LENGTH, LENGTH))
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
                pygame.draw.line(self.surface, (0, 0, 0), points[0], points[1], LENGTH//10)
    def get_surf(self):
        return self.surface
    def draw_wall(self, pos, place):
        if pos[0] <= LENGTH // 10:
            if place % SIZE == 0:
                return None
            self.walls[Walls.LEFT.value] = not self.walls[Walls.LEFT.value]
            self.draw()
            return Walls.LEFT
        if pos[0] >= LENGTH - (LENGTH  // 10):
            if place % SIZE == 39:
                return None
            self.walls[Walls.RIGHT.value] = not self.walls[Walls.RIGHT.value]
            self.draw()
            return Walls.RIGHT
        if pos[1] <= LENGTH // 10:
            if place // SIZE == 0:
                return None
            self.walls[Walls.TOP.value] = not self.walls[Walls.TOP.value]
            self.draw()
            return Walls.TOP
        if pos[1] >= LENGTH - (LENGTH  // 10):
            if place // SIZE == 39:
                return None
            self.walls[Walls.BOTTOM.value] = not self.walls[Walls.BOTTOM.value]
            self.draw()
            return Walls.BOTTOM
        return None

class Maze():
    def __init__(self, blocks, size):
        self.blocks = blocks
        self.size = size
        self.surface = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
        self.draw()
    def draw(self):
        self.surface.fill((255, 255, 255))
        for position, block in enumerate(self.blocks):
            self.surface.blit(block.get_surf(), ((position % self.size) * LENGTH, (position // self.size) * LENGTH))
    def update_wall(self, pos):
        absolute_pos = [i // 1 for i in pos]
        pos = [(i / LENGTH) // 1 for i in pos]
        place = int(pos[0] + (self.size * pos[1]))
        wall = self.blocks[place].draw_wall([i % LENGTH for i in absolute_pos], place)
        if wall == Walls.LEFT and place % self.size != 0:
            self.blocks[place-1].walls[Walls.RIGHT.value] = not self.blocks[place-1].walls[Walls.RIGHT.value]
            self.blocks[place-1].draw()
        elif wall == Walls.RIGHT and place % self.size != self.size - 1:
            self.blocks[place+1].walls[Walls.LEFT.value] = not self.blocks[place+1].walls[Walls.LEFT.value]
            self.blocks[place+1].draw()
        elif wall == Walls.TOP and place // self.size != 0:
            self.blocks[place-self.size].walls[Walls.BOTTOM.value] = not self.blocks[place-self.size].walls[Walls.BOTTOM.value]
            self.blocks[place-self.size].draw()
        elif wall == Walls.BOTTOM and place // self.size != self.size - 1:
            self.blocks[place+self.size].walls[Walls.TOP.value] = not self.blocks[place+self.size].walls[Walls.TOP.value]
            self.blocks[place+self.size].draw()
        self.draw()
