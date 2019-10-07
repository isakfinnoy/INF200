__author__ = 'Isak Finnoy'
__email__ = 'isfi@nmbu.no'


def char_counts(textfilename):  # function that counts characters
    with open(textfilename, encoding='utf-8') as file:  # opening the text file
        data = file.read().replace('\n', '')  # converting file into a single string
    file.close()  # closing text file
    result = [0]*256  # creating a list with 256 zeros
    for char in data:
        result[ord(char)] += 1  # looping over data, summing up each character to its respective index
    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
