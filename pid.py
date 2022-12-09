#!/usr/bin/env python3
import gymnasium as gym

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

class Controller:
    def __init__(self):
        self.cart = PD(kp=1, kd=100, goal=0)
        self.pole = PD(kp=5, kd=100, goal=0)

    def observe(self, cart_position, pole_angle):
        u_cart = self.cart.observe(cart_position)
        u_pole = self.pole.observe(pole_angle)
        action = 1 if u_pole + u_cart < 0 else 0
        return action

if __name__ == "__main__":
    controller = Controller()

    env = gym.make("CartPole-v1", render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        cart_position = observation[0]
        pole_angle = observation[2]
        action = controller.observe(cart_position, pole_angle)

        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()

    env.close()
