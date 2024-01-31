#!/usr/bin/python3
"""
   Change comes from within
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to
    meet a given amount total.
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    """Optimizations:"""
    coins.sort()  # Sort coins in ascending order for early termination

    for coin in coins:
        for i in range(coin, total + 1):
            """Early termination if coin is too large"""
            if coin > i:
                break
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
