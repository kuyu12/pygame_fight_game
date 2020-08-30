import os

import tensorflow as tf
from tf_agents.agents.dqn import dqn_agent
from tf_agents.environments import tf_py_environment
from tf_agents.networks import q_network
from tf_agents.policies import policy_saver
from tf_agents.policies.policy_saver import PolicySaver
from tf_agents.replay_buffers import tf_uniform_replay_buffer
from tf_agents.trajectories import trajectory
from tf_agents.utils import common
import pandas as pd
from tf_agents.LF_env import littleFighterEnv
import matplotlib.pyplot as plt
import pickle
from tf_agents.blackjack_env import CardGameEnv
from tf_agents.trajectories import time_step as ts

# env = littleFighterEnv()
# env = tf_py_environment.TFPyEnvironment(env)
# time_step = env.reset()
# policy = tf.saved_model.load('temp')
# a = policy.action(time_step)
# print(a)

#
#
# env = littleFighterEnv()
# env = tf_py_environment.TFPyEnvironment(env)
#
# q_net = q_network.QNetwork(env.observation_spec(), env.action_spec(), fc_layer_params=(100,))
# optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=0.001)
#
# train_step_counter = tf.Variable(0)
# agent = dqn_agent.DqnAgent(env.time_step_spec(),
#                            env.action_spec(),
#                            q_network=q_net,
#                            optimizer=optimizer,
#                            td_errors_loss_fn=common.element_wise_squared_loss,
#                            train_step_counter=train_step_counter)
#
# agent.initialize()
#
#
# def compute_avg_return(environment, policy, num_episodes=10):
#     total_return = 0.0
#     for _ in range(num_episodes):
#
#         time_step = environment.reset()
#         episode_return = 0.0
#
#         while not time_step.is_last():
#             action_step = policy.action(time_step)
#             time_step = environment.step(action_step.action)
#             episode_return += time_step.reward
#         total_return += episode_return
#
#     avg_return = total_return / num_episodes
#     return avg_return.numpy()[0]
#
#
# # Evaluate the agent's policy once before training.
# avg_return = compute_avg_return(env, agent.policy, 5)
# returns = [avg_return]
# replay_buffer = tf_uniform_replay_buffer.TFUniformReplayBuffer(data_spec=agent.collect_data_spec,
#                                                                batch_size=env.batch_size,
#                                                                max_length=20000)
#
# def collect_step(environment, policy, buffer):
#     time_step = environment.current_time_step()
#     action_step = policy.action(time_step)
#     next_time_step = environment.step(action_step.action)
#     traj = trajectory.from_transition(time_step, action_step, next_time_step)
#
#     # Add trajectory to the replay buffer
#     buffer.add_batch(traj)
#
#
# collect_steps_per_iteration = 1
# batch_size = 64
# dataset = replay_buffer.as_dataset(num_parallel_calls=3,
#                                    sample_batch_size=batch_size,
#                                    num_steps=2).prefetch(3)
# iterator = iter(dataset)
# num_iterations = 20000
# env.reset()
# for _ in range(batch_size):
#     collect_step(env, agent.policy, replay_buffer)
#
# for _ in range(num_iterations):
#     # Collect a few steps using collect_policy and save to the replay buffer.
#     for _ in range(collect_steps_per_iteration):
#         collect_step(env, agent.collect_policy, replay_buffer)
#
#     # Sample a batch of data from the buffer and update the agent's network.
#     experience, unused_info = next(iterator)
#     train_loss = agent.train(experience).loss
#
#     step = agent.train_step_counter.numpy()
#
#     # Print loss every 200 steps.
#     if step % 200 == 0:
#         print('step = {0}: loss = {1}'.format(step, train_loss))
#
#     # Evaluate agent's performance every 1000 steps.
#     if step % 1000 == 0:
#         avg_return = compute_avg_return(env, agent.policy, 5)
#         print('step = {0}: Average Return = {1}'.format(step, avg_return))
#         returns.append(avg_return)
#
# pd.DataFrame(returns).plot()
# print(returns)
# plt.show()
#
#
#
#
#
# for num in range(10):
#     step = env.reset()
#     time_step = env.current_time_step()
#     while not time_step.is_last().numpy()[0]:
#       time_step = env.current_time_step()
#       print(time_step.observation.numpy())
#       action_step = agent.policy.action(time_step)
#       next_time_step = env.step(action_step.action)
#
#     print("end")
#
#
# PolicySaver(agent.policy).save('temp')
#
