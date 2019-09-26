__author__ = 'Isak Finnoy'
__email__ = 'isfi@nmbu.no'


def bubble_sort(data1):  # function that sorts cards according to their value

    sorted_data = list(data1)  # converts tuple into list to allow for necessary operations
    cards = len(sorted_data)  # stores the length of the list as 'cards'
    for i in range(cards):  # for-loop to simulate each round of shuffling
        for j in range(0, cards - i - 1):  # for-loop to shuffle cards according to its index relative to 'j'
            if sorted_data[j] > sorted_data[j + 1]:  # if-test to check card-values relative to each other
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]  # shuffling cards according to
                                                                                         # the conditions
    return tuple(sorted_data)  # returning the processed list as a tuple


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
