#!/usr/bin/python3
'''UTF-8 validation module.
'''


def validUTF8(data):
    '''Checks if a given list of integers represents valid UTF-8 codepoints.
    '''
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            sp = 4
            if n - i >= sp:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + sp],
                ))
                if not all(next_body):
                    return False
                skip = sp - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            sp = 3
            if n - i >= sp:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + sp],
                ))
                if not all(next_body):
                    return False
                skip = sp - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            sp = 2
            if n - i >= sp:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + sp],
                ))
                if not all(next_body):
                    return False
                skip = sp - 1
            else:
                return False
        else:
            return False
    return True
