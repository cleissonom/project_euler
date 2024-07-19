# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

from helpers import measure_time


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Brute force
@measure_time
def solution(target=2_000_000):
    primes = [2, 3, 5, 7]

    for n in range(11, target):
        if is_prime(n):
            primes.append(n)

    return sum(primes)


# Less brutal
@measure_time
def solution2(target=2_000_000):
    result = 17  # Initial value
    n = 11

    while n < target:
        if is_prime(n):
            result += n
        n += 2

        if is_prime(n) and n <= target:
            result += n
        n += 4

    return result


# Sieve of Eratosthenes
@measure_time
def solution3(target=2_000_000):
    sievebound = (target - 1) // 2
    sieve = [False] * (sievebound + 1)
    crosslimit = int(target**0.5 - 1) // 2

    for i in range(1, crosslimit + 1):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sievebound + 1, 2 * i + 1):
                sieve[j] = True

    result = 2
    for i in range(1, sievebound + 1):
        if not sieve[i]:
            result += 2 * i + 1

    return result


# Map all multuples of base primes to False
@measure_time
def solution4(target=2_000_000):
    sieve = [True] * target
    sieve[0] = False  # 1 is not a prime number

    for n in range(2, target + 1):
        if sieve[n - 1]:
            for multiple in range(n * 2, target + 1, n):
                sieve[multiple - 1] = False

    return sum(i + 1 for i in range(len(sieve)) if sieve[i])


def main():
    solution()
    # Result: 142913828922
    #  Real time: 3.54486271 seconds
    #  CPU time: 3.53542000 seconds
    solution2()
    # Result: 142913828922
    #  Real time: 3.38299992 seconds
    #  CPU time: 3.35987200 seconds
    solution3()
    # Result: 142913828922
    #  Real time: 0.08268404 seconds
    #  CPU time: 0.08209200 seconds
    solution4()
    # Result: 142913828922
    #  Real time: 0.42478658 seconds
    #  CPU time: 0.42295600 seconds


if __name__ == "__main__":
    main()
