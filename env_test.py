from env import MazeAIEnv

env = MazeAIEnv()
env.reset()
time = 100
for _ in range(time):
    env.render()
    env.step(env.action_space.sample())
env.close()
