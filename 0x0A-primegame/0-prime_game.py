#!/usr/bin/python3
'''A module to determine prime numbers
'''


def isWinner(x, nums):
    """Finds the winner of a prime game.
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0

    # generate prime numbers up to the max value in the list of "nums"
    max_num = max(nums)
    primes = [True for _ in range(1, max_num + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, max_num + 1, i):
            primes[j - 1] = False
    '''filter the number of primes that are less than 'max_num'
    in the given list of 'nums' for each round.
    '''
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
