#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(n):
    """Generate a list indicating prime numbers up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def count_primes_up_to(sieve, n):
    """Count the number of primes up to n using the precomputed sieve."""
    return sum(sieve[2:n+1])


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if x < 1 or not nums:
        return None

    # Find the maximum n value in nums to precompute primes
    max_n = max(nums)
    sieve = sieve_of_eratosthenes(max_n)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        prime_count = count_primes_up_to(sieve, n)

        # If the number of primes is odd, Maria wins (she goes first)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
