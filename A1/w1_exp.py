#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
  Last Modified by: Andrew Jacobsen, Victor Silva, Mohammad M. Ajallooeian
  Last Modified on: 16/9/2017

  Experiment runs 2000 runs, each 1000 steps, of an n-armed bandit problem
"""

from rl_glue import *  # Required for RL-Glue
RLGlue("w1_env", "w1_agent")

import numpy as np
import sys

def save_results(data, data_size, filename): # data: floating point, data_size: integer, filename: string
    with open(filename, "w") as data_file:
        for i in range(data_size):
            data_file.write("{0}\n".format(data[i]))

def getOptimalAction():
    return int(RL_env_message("get optimal action"))

def setoption(): # allow the user to choose from two options
    option = input("\nPlease input you option('0'for epsilon=0 Q1=5, '1'for eosilon=0.1 Q1=0):")
    RL_agent_message(option)

if __name__ == "__main__":
    num_runs = 2000
    max_steps = 1000

    # array to store the results of each step
    optimal_action = np.zeros(max_steps)

    setoption()

    print "\nPrinting one dot for every run: {0} total Runs to complete".format(num_runs)
    for k in range(num_runs):
        RL_init()

        optimalOption = getOptimalAction()

        RL_start()
        for i in range(max_steps):
            # RL_step returns (reward, state, action, is_terminal); we need only the
            # action in this problem
            action = RL_step()[2]

            '''
            check if action taken was optimal

            you need to get the optimal action; see the news/notices
            announcement on eClass for how to implement this
            '''
            # update your optimal action statistic here
                #if getOptimalAction()/i == 0:
                    #optimal_action[i] = getOptimalAction()

            if action[0] == optimalOption:
                optimal_action[i] += 1


        RL_cleanup()
        print ".",
        sys.stdout.flush()

    save_results(optimal_action / num_runs, max_steps, "RL_EXP_OUT.dat")
    print "\nDone"
