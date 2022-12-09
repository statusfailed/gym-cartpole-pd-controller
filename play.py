#!/usr/bin/env python3
import gymnasium as gym
from gymnasium.utils.play import play
keys = { "a": 0, "d": 1 } # map keys 'a' and 'd' to actions left and right.
env = gym.make("CartPole-v1", render_mode="rgb_array")
play(env, keys_to_action=keys, noop=0) # noop=0 means default action is move left
