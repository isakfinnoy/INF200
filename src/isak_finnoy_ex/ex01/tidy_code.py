from random import randint as dice

__author__ = 'Isak Finnoy'
__email__ = 'isfi@nmbu.no'

"""This is a game of two dices, where the user is trying to guess the correct sum of the two dices,
decided by the random.randint function. The max number of valid guess attempts are 3, though you can make as many 
invalid guesses (guess < 2) as you like, as they will not be counted by the program. 
"""

def guess_input():
    guess = 0
    while guess < 2:  # changed 1 to 2 since the sum of two dices can never be less than 2
        guess = int(input('Your guess: '))
    return guess

def dices_roll():
    return dice(1, 6) + dice(1, 6)

def compare_sum_and_guess(sum_eyes, your_guess):
    return sum_eyes == your_guess

if __name__ == '__main__':

    win = False
    remaining_attempts = 3
    sum_eyes = dices_roll()
    while not win and max_attempts > 0:
        your_guess = guess_input()
        win = compare_sum_and_guess(sum_eyes, your_guess)
        if not win:
            print('Wrong, try again!')
            remaining_attempts -= 1

    if remaining_attempts > 0:
        print('You won {} points.'.format(remaining_attempts))
    else:
        print('You lost. Correct answer: {}.'.format(sum_eyes))