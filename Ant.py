'''
This file represents one ant in the given project. Every ant is given an ID at creation,
and has a job (currently either 0 or 1); will be refactored into a vector later).

It also has a cumulative sum (CuSum) that it keeps track of whenever it encounters an ant

'''

import random

class Ant(object):

    def __init__(self, id_input, job_input, beta_input):

        self.ID = id_input
        self.job = job_input
        self.beta = beta_input

        self.mode = 0 #modes are: 0 is updating, 1 is triggered, and 2 is resting
        self.future_job = 0
        self.counter = 0

        self.cusum = [0, 0]

    def print_me(self):

        print "Hello, my name is " + str(self.ID) + " and my job is " + str(self.job)

        print "My CuSum is "

        print self.cusum

    def update_cusum(self, other_ant):

        for i in range(len(self.cusum)):
            if i == other_ant.job:
                self.cusum[i] += 1
            else:
                self.cusum[i] = 0



    def choose_job(self):


        return random.randint(0,1) #right now chooses a random number between 0 and 1

    def update_ant(self):

        if self.mode == 0:

            for i in range(len(self.cusum)):
                if self.cusum[i] > self.beta:
                    self.future_job = self.choose_job()
                    self.mode = 1
                    self.counter = self.beta

            return

        if self.mode == 1:

            if self.counter is 0:
                self.mode = 2
                self.job = self.future_job
                self.counter = self.beta
            else:
                self.counter -= 1

            return

        if self.mode == 2:

            if self.counter is 0:
                self.cusum = [0, 0]
                self.mode = 0

            else:
                self.counter -= 1










