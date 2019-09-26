def char_counts(textfilename):
    with open(textfilename, encoding = 'utf-8') as file:
        data = file.read().replace('\n', '')
    result = [0] * 256
    for char in data:
        result[ord(char)] += 1
    return result



if __name__ == '__main__':

    filename = 'char_counts.py'
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