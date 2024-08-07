#!/usr/bin/python3
"""0. Minimum Operations"""


def minOperations(n):
    """Prime Factorization Concept"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            # While n is divisible by factor, add the factor
            # to operations and divide n by factor
            operations += factor
            n /= factor
        # Move to the next factor
        factor += 1
    return operations
