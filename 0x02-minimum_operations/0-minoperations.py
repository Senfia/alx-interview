#!/usr/bin/python3
'''calculates the fewest number of operations needed
to result in exactly n H characters in the file.
'''


def min_operations(n):
    '''Returns an integer.
    If n is imposible to achieve, return 0
    '''
    if not isinstance(n, int):
        return 0

    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    result = 0
    for factor in factors:
        result += factor

    return result
