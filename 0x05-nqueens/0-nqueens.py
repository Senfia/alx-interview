#!/usr/bin/python3
'''N queens.
'''
import sys


solutions = []

n = 0
'''Size of the chessboard.
'''
opts = None


def get_input():
    '''Retrieves and validates it's argument.
    '''
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(opts0, opts1):
    '''Checks if the positions of two queens are in an attacking mode.
    '''
    if (opts0[0] == opts1[0]) or (opts0[1] == opts1[1]):
        return True
    return abs(opts0[0] - opts1[0]) == abs(opts0[1] - opts1[1])


def group_exists(group):
    '''Verifies if a group is present in the list of solution.
    '''
    global solutions
    for stn in solutions:
        i = 0
        for stn_opts in stn:
            for grp_opts in group:
                if stn_opts[0] == grp_opts[0] and stn_opts[1] == grp_opts[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    '''Develops a solution for the N-Queens problem.
    '''
    global solutions
    global n
    if row == n:
        temp0 = group.copy()
        if not group_exists(temp0):
            solutions.append(temp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([opts[a]]) * len(group), group)
            used_optsitions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(opts[a].copy())
            if not any(used_optsitions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solution():
    '''Gets the solution for the given chessboard size.
    '''
    global opts, n
    opts = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solution()
for solution in solutions:
    print(solution)
