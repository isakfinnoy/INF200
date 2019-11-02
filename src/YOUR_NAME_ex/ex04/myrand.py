# -*- coding: utf-8 -*-

__author__ = 'Isak Finnøy'
__email__ = 'isfi@nmbu.no'


class LCGRand:

    def __init__(self, seed):
        """
        :param seed: arbitrary input
        """
        self.seed = seed
        self.a = 7 ** 5
        self.m = 2 ** 31 - 1

    def rand(self):
        """
        Calculates next random number with the LCG method
        """
        self.seed = self.a * self.seed % self.m
        return self.seed


class ListRand:

    def __init__(self, lis):
        """
        :param lis: arbitrary list
        """
        self.lis = lis
        self.idx = 0
        self.len = len(self.lis) - 1

    def rand(self):
        """
        Returns next "random" number from an arbitrary list
        """
        if self.idx > self.len:
            raise RuntimeError('The index exceeds length of list')
        r = self.lis[self.idx]
        self.idx += 1
        return r


if __name__ == "__main__":
    list_random = ListRand([3, 5, 9, 2, 1, 4])
    print(list_random.rand())
    print(list_random.rand())
    lcg = LCGRand(514)
    print(lcg.rand())
    print(lcg.rand())
