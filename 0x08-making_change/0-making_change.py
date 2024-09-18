#!/usr/bin/python3
"""0. Change comes from within"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the fewest coins needed
    # for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make a total of 0

    # Iterate over each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf, it means the total
    # cannot be reached with the given coins
    return dp[total] if dp[total] != float('inf') else -1
