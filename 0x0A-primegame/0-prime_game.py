#!/usr/bin/python3
'''A module to determin prime numbers
'''


def is_prime(num):
    '''
       Returns a prime number
    '''
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def simulate_game(n):
    primes = [i for i in range(2, n+1) if is_prime(i)]
    turn = 0  # 0 for Maria, 1 for Ben
    while True:
        if not primes:
            return turn  # No prime numbers left, the other player wins
        if turn == 0:
            for prime in primes:
                multiples = [prime * i for i in range(1, (n // prime) + 1)]
                for multiple in multiples:
                    if multiple in primes:
                        primes.remove(multiple)
            turn = 1  # Switch turn to Ben
        else:
            for prime in primes:
                multiples = [prime * i for i in range(1, (n // prime) + 1)]
                for multiple in multiples:
                    if multiple in primes:
                        primes.remove(multiple)
            turn = 0  # Switch turn to Maria


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = simulate_game(n)
        if winner == 0:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
