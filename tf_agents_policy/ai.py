from tf_agents.environments import tf_py_environment

from tf_agents_policy.LF_env import littleFighterEnv
import tensorflow as tf


def get_env(location):
    env = littleFighterEnv()
    env.set_location(location)
    return tf_py_environment.TFPyEnvironment(env)


policy = tf.saved_model.load('tf_agents_policy/temp')
