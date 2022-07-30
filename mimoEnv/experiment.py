

""" Simple script to view the showroom. We perform no training and MIMo takes no actions.
"""

import gym
import time
import numpy as np
import mimoEnv


def main():
    """ Creates the environment and takes 200 time steps. MIMo takes no actions.
    The environment is rendered to an interactive window.
    """

    env = gym.make("MIMoExperiment-v0")

    max_steps = 1000

    _ = env.reset()

    start = time.time()
    for step in range(max_steps):
        action = np.zeros(env.action_space.shape)
        obs, reward, done, info = env.step(action)
        env.render()
        if step > 20:
            print("yay")
        if done:
            print("DONE")
            env.reset()

    print("Elapsed time: ", time.time() - start, "Simulation time:", max_steps*env.dt)
    env.close()


if __name__ == "__main__":
    main()