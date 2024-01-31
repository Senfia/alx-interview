#!/usr/bin/python3
"""
   Change comes from within
"""


def makeChange(coins, total):
    '''
       determines the fewest number of coins needed
       to meet a given amount total
    '''
    if total <= 0:
        return 0

    '''
    Initialize an array to store the minimum number of coins
    needed for each total
    '''
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make a total of 0
    dp[0] = 0

    '''
    Iterate through each coin and update the minimum number
    of coins needed for each total
    '''
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    '''If the final value at the total is still infinity,
    it means the total cannot be met
    '''
    return dp[total] if dp[total] != float('inf') else -1
