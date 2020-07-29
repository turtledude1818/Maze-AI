from env import MazeAIEnv

env = MazeAIEnv()
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
env.close()
