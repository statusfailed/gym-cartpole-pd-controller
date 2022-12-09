#!/usr/bin/env python3

import numpy as np
import gymnasium as gym
from gymnasium.utils.play import play

import gymnasium as gym

from gymnasium.utils.play import play

lunar_keys = {
    "w": 2,
    "a": 1,
    "s": 4,
    "d": 3,
}
lunar_noop = 0
# play(gym.make("CartPole-v1", render_mode="rgb_array"), keys_to_action=lunar_keys, noop=lunar_noop)

cp_keys = { "a": 0, "d": 1 }
cp_noop = 0

keys = cp_keys
noop = cp_noop
env = gym.make("CartPole-v1", render_mode="rgb_array")
play(env, keys_to_action=keys, noop=noop)
