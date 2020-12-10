import multiagent.scenarios as scenarios
from multiagent.environment import MultiAgentEnv


def make_env(args):
    """Make multi-agent particle environment
    Ref: https://github.com/openai/maddpg/blob/master/experiments/train.py
    """
    scenario = scenarios.load(args.env_name + ".py").Scenario()
    world = scenario.make_world()
    done_callback = None

    env = MultiAgentEnv(
        world,
        reset_callback=scenario.reset_world,
        reward_callback=scenario.reward,
        observation_callback=scenario.observation,
        done_callback=done_callback)

    return env
