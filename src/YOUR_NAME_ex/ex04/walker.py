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


if __name__ == "__main__":
    dist = [1, 2, 5, 10, 20, 50, 100]
    steps_pr_dist = []
    for i, el in enumerate(dist):
        nr_steps = [walk_home(0, el) for _ in range(5)]
        steps_pr_dist.append(nr_steps)
        print('Distance: {0:4d} -> Path lengths: {1}'.format(el,
                                                             sorted(
                                                                 steps_pr_dist[
                                                                     i])))
