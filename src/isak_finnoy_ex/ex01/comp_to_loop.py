__author__ = 'Isak Finnoy'
__email__ = 'isfi@nmbu.no'

def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]

def squares_by_loop(n):
    liste = []
    for i in range(n):
        if i % 3 == 1:
            liste.append(i ** 2)
    return liste


if __name__ == '__main__':
    if squares_by_comp(n) != squares_by_loop(n):
        print('ERROR!')