import os
import argparse
import random
import torch
import numpy as np
from gym_env import make_env
from misc.utils import set_log 
from tensorboardX import SummaryWriter


def main(args):
    # Set logging
    if not os.path.exists("./log"):
        os.makedirs("./log")

    log = set_log(args)
    tb_writer = SummaryWriter('./log/tb_{0}'.format(args.log_name))

    # Set env
    env = make_env(args)

    # Set seeds
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    env.seed(args.seed)

    # Start training
    observations = env.reset()
    while True:
        # Get actions
        actions = [
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0]]

        # Take step in env
        new_observations, rewards, done, info = env.step(actions)

        # For next timestep
        observations = new_observations


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="meta-mapg")

    # Env
    parser.add_argument(
        "--env-name", type=str, default="",
        help="OpenAI gym environment name")
    parser.add_argument(
        "--ep-horizon", type=int, default=int(500),
        help="Episode is terminated when max timestep is reached")
    parser.add_argument(
        "--n-agent", type=int, default=2,
        help="Number of agents in a shared environment")

    # Misc
    parser.add_argument(
        "--seed", type=int, default=1, 
        help="Sets Gym, PyTorch and Numpy seeds")
    parser.add_argument(
        "--prefix", type=str, default="", 
        help="Prefix for tb_writer and logging")

    args = parser.parse_args()

    # Set log name
    args.log_name = "env::%s_seed::%s_prefix::%s_log" % (args.env_name, args.seed, args.prefix)

    main(args=args)
