__author__ = 'Isak Finnoy'
__email__ = 'isfi@nmbu.no'


def entropy(message):  # estimates the entropy of a string
    import math   # imports the math module
    import letter_counts  # imports self-made module
    freq = letter_counts.letter_freq(message)  # uses letter_freq to count frequency of characters in string
    teller = len(message)  # sets the denominator equal to the length of the string
    liste = []   # creates an empty list
    for i in freq.keys():  # loops over the keys in the dictionary letter_freq returns
        p_entropy = -(freq[i]/teller*(math.log2(freq[i]/teller)))  # calculates the entropy for a single letter
        liste.append(p_entropy)  # adds all the letters into the empty list
    entropy_value = sum(liste)  # sums the list to calculate the entropy of the whole string
    return entropy_value


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
