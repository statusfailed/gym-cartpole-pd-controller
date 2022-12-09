#!/usr/bin/env python3
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

class PD:
    def __init__(self, kp, kd, goal):
        self.kp = kp
        self.kd = kd
        self.goal = goal
        self.last_error = 0

    def observe(self, x):
        error = self.goal - x
        d_error = error - self.last_error
        self.last_error = error
        return self.kp * error + self.kd * d_error

if __name__ == "__main__":
    controller = PD(kp=5, kd=100, goal=0)

    for _ in range(1000):
        pole_angle = observation[2]
        control_output = controller.observe(pole_angle)
        action = int(control_output < 0)

        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()

    env.close()
