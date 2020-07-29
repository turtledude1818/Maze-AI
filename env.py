import gym
from gym import spaces
import pygame
from pygame.locals import *
from maze import *
import sys

class MazeAIEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(MazeAIEnv, self).__init__()

        pygame.init()
        self.clock = pygame.time.Clock()
        self.maze = MazeCreation().create_random_maze()
        self.display_surf = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 20)) 
        pygame.display.set_caption("Maze")  
        self.display_surf.fill((255, 255, 255))
        self.display_surf.blit(self.maze.surface, (0, 0))

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Tuple(list((spaces.Box(low=0, high=14, shape=(1, 4)) for x in range(4))))
    def step(self, action):
        self._take_action(action)

        obs = self._observe
        done = self.maze.blocks[SIZE**2-1] == self.maze.agent_block
        reward = 1000 if done else -1

        return obs, reward, done, {}

    def reset(self):
        self.maze = MazeCreation().create_random_maze()
        self.display_surf.fill((255, 255, 255))
        self.display_surf.blit(self.maze.surface, (0, 0))
        #self.observation_space = spaces.Box(low=0, high=14, shape=(1, 1, 1, 1, 4), dtype=np.int8)
        self.observation_space = spaces.Tuple(list((spaces.Box(low=0, high=14, shape=(1, 4)) for x in range(4))))
        for x in self.observation_space.spaces:
            x.shape = list(x.shape)

        return self._observe()
    def render(self, mode='human'):
        self.display_surf.fill((255, 255, 255))

        self.maze.draw()
        self.display_surf.blit(self.maze.surface, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                self.maze.update_wall(event.pos)
        pygame.display.update()
        self.clock.tick(CLOCK_SPEED)
    def close(self):
        pygame.quit()
    def _observe(self):
        obs = list((list() for x in range(4)))
        for i in range(4):
            curr = self.maze.agent_block
            while not curr.walls[i]:
                curr = self.maze.blocks[self.maze.get_side(self.maze.blocks.index(curr), i)]
                obs[i].append(tuple(curr.walls))
        for pos, i in enumerate(obs):
            self.observation_space.spaces[pos].shape[0] = len(i)
    def _take_action(self, action):
        if self.maze.agent_block.walls[action]:
            return
        self.maze.move_agent(action)
