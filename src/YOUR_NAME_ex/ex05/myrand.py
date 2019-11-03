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

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        """
        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError()
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError()
        if self.num_generated_numbers == self.length:
            raise StopIteration

        next_random_number = self.generator.rand()
        self.num_generated_numbers += 1

        return next_random_number


if __name__ == '__main__':
    rng_generator = LCGRand(1)
    for rand in rng_generator.random_sequence(10):
        print(rand)
    for i, rand in enumerate(
            rng_generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
