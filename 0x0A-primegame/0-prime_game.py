#!/usr/bin/python3
'''A module to determine prime numbers
'''


def isWinner(x, nums):
    """Finds the winner of a prime game.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0

    # generate prime numbers up to the maximum value in the given list of "nums"
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    '''filter the number of primes that are less than 'n' in the given list
    of 'nums' for each round.
    '''
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
