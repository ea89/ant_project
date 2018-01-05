'''
This is the main class that runs the simulation.
'''
from __future__ import division
from Ant import Ant

import numpy

class SimulationMain:


    def __init__(self, beta, gamma, sim_length, ants_number):
        self.beta = beta
        self.gamma = gamma
        self.sim_length = sim_length
        self.ants_number = ants_number

        self.ant_list = []
        self.simulation_ratios = []
        self.turn_count = 0

        self.make_all_ants()

    def make_ant(self, id, job, beta):
        a = Ant(id, job, beta)
        self.ant_list.append(a)

        return self.ant_list

    def make_all_ants(self):

        for i in range(0, self.ants_number):

            if i < self.ants_number/2:
                self.make_ant(i, 0, self.beta)
            else:
                self.make_ant(i, 1, self.beta)

    def print_all_ants(self):

        for ant in self.ant_list:
            ant.print_me()


    def step(self):
        num_ones = 0;

        x = numpy.random.permutation(len(self.ant_list))

        for i in range(len(self.ant_list)):
            self.ant_list[i].update_cusum(self.ant_list[x[i]])
            self.ant_list[i].update_ant()
            if self.ant_list[i].job is 1:
                num_ones += 1


        self.simulation_ratios.append(num_ones/len(self.ant_list))

    def run_sim(self):

        for i in range(0, self.sim_length):
            self.step()

            self.turn_count += 1 #first turn is turn 1

            if self.turn_count is self.gamma:

                self.ants_to_keep = []

                for ant in self.ant_list:
                    if ant.job is 1:
                        self.ants_to_keep.append(ant)

                self.ant_list = self.ants_to_keep




beta = 10
gamma = 5
sim_length = 100
ants_number = 10000

s = SimulationMain(beta, gamma, sim_length, ants_number)

s.run_sim()

print s.simulation_ratios
