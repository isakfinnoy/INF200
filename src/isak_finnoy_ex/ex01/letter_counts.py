__author__ = 'Isak Finnoy'
__email__ = 'isfi@nmbu.no'

def letter_freq(txt):
    dict = {}
    txt = txt.lower()
    for n in txt:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()):
        print('{:3}{:10}'.format(letter, count))
