#!/usr/bin/env python3
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()
for _ in range(1000):
    action = 1 if observation[0] < 0 else 0
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()
env.close()
