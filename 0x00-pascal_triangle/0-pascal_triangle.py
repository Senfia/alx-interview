#!/usr/bin/python3
'''Pascal's triangle.
'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing
       the Pascal’s triangle of n
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle

    i = 0
    while i < n:
        line = []
        j = 0
        while j < (i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            j += 1
        triangle.append(line)
        i += 1

    return triangle