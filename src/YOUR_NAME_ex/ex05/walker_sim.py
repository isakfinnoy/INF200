# -*- coding: utf-8 -*-

__author__ = 'Isak Finnøy'
__email__ = 'isfi@nmbu.no'

import random

"""
importing necessary modules
"""


class Walker:
    """
    Class that simulates movement of a person in a one-dimensional world (
    moving along a line)
    """

    def __init__(self, x0, h):
        """
        :param x0: start position of person
        :param h: destination of person
        """
        self.x0 = x0
        self.x = x0
        self.step = 0
        self.h = h

    def move(self):
        """
        Function that simulation one step along the line
        """
        rnd = random.randint(0, 1)
        if rnd == 0:
            rnd = -1
        self.x += rnd
        self.step += 1


    def is_at_home(self):
        """
        Checks if person has arrived at destination
        """
        if self.x == self.h:
            return True
        else:
            return False

    def get_position(self):
        """
        Returns the position of the person
        """
        return self.x

    def get_steps(self):
        """
        Returns the number of steps between initial position and destination
        """
        return self.step


def walk_home(x0, h):
    """
    Returns the number of steps for a given destination and start position
    """
    walk = Walker(x0, h)
    pos = x0

    while pos != h:
        walk.move()
        pos = walk.get_position()
    return walk.get_steps()


class Simulation:

    def __init__(self, start, home, seed):

        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        self.seed = seed



    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walker = Walker(self.start, self.home)

        while not walker.is_at_home()
            walker.move()

        return walker.get_steps()



    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        random.seed(self.seed)
        step_pr_sim = [self.single_walk() for _ in range(num_walks)]
        return step_pr_sim


if __name__ == "__main__":
    sit1 = Simulation(0, 10, 12345)
    sit2 = Simulation(10, 0, 12345)
    sit3 = Simulation(0, 10, 54321)
    sit4 = Simulation(10, 0, 54321)

    lis1 = sit1.run_simulation(20)
    lis2 = sit1.run_simulation(20)
    lis3 = sit2.run_simulation(20)
    lis4 = sit2.run_simulation(20)
    lis5 = sit3.run_simulation(20)
    lis6 = sit4.run_simulation(20)

    print(lis1)
    print(lis2)
    print(lis3)
    print(lis4)
    print(lis5)
    print(lis6)