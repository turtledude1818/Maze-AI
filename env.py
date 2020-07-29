import gym
from gym import spaces
import pygame
from pygame.locals import *
from maze import *
import numpy as np

class MazeAIEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(MazeAIEnv, self).__init__()

        pygame.init()
        self.clock = pygame.time.Clock()
        self.maze = MazeCreation().create_random_maze()
        self.display_surf = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 20))   
        self.display_surf.fill((255, 255, 255))
        self.display_surf.blit(self.maze.surface, (0, 0))

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=14, shape=(1, 4, 4), dtype=np.int8)
    def step(self, action):
        self._take_action(action)
    def reset(self):
        self.maze = MazeCreation().create_random_maze()
        self.display_surf.fill((255, 255, 255))
        self.display_surf.blit(self.maze.surface, (0, 0))
        #self.observation_space = spaces.Box(low=0, high=14, shape=(1, 1, 1, 1, 4), dtype=np.int8)
        self.observation_space = spaces.Tuple((spaces.Box(low=0, high=14, shape=(1, 4)) for x in range(4)))

        return self._observe()
    def render(self, mode='human'):
        return super().render(mode=mode)
    def close(self):
        pygame.quit()
    def _observe(self):
        obs = tuple((tuple() for x in range(4)))
        for i in range(4):
            curr = self.maze.agent_block
            while not curr.walls(i):
                curr = self.maze.blocks[self.maze.get_side(self.maze.blocks.index(curr), i)]
                obs[i].append(tuple(curr.walls))
        for pos, i in enumerate(obs):
            self.observation_space.spaces[pos].shape[0] = len(i)

        return obs
    def _take_action(self, action):
        pass
