import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class StrikeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        self._x = 1
    
    def step(self, action):
        self._x += 1
        reward = self._x + 2
        done = True if self._x>10 else False 
        return np.array([self._x]), reward, done, {}

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        return np.array([0.0])
    
    def render(self, mode='human'):
        return None

    def close(self):
        return None