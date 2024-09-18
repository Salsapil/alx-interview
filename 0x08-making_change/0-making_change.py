#!/usr/bin/python3
"""0. Change comes from within"""
from collections import deque


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Set to keep track of visited totals
    # to avoid re-processing
    visited = set()
    visited.add(0)

    # Initialize the queue with a
    # tuple of (current total, number of coins used)
    queue = deque([(0, 0)])

    # Perform BFS
    while queue:
        current_total, coin_count = queue.popleft()

        # Try all coins
        for coin in coins:
            new_total = current_total + coin

            # If we reach the total, return the number of coins used
            if new_total == total:
                return coin_count + 1

            # If the new total is less than total
            # and has not been visited, add to queue
            if new_total < total and new_total not in visited:
                visited.add(new_total)
                queue.append((new_total, coin_count + 1))

    # If no solution was found, return -1
    return -1
