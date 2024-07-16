# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a > b > c ,for which, a^2 = b^2 + c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

from helpers import measure_time


# Brute force
@measure_time
def solution(target=1000):
    for a in range(1, target + 1):
        for b in range(a + 1, target + 1):
            c = target - a - b
            if a * a + b * b == c * c:
                return a * b * c


# Reduced search
@measure_time
def solution2(target=1000):
    for a in range(1, target // 3):
        for b in range(a, target // 2):
            c = target - a - b
            if a * a + b * b == c * c:
                return a * b * c


def main():
    solution()
    # Result: 31875000
    #  Real time: 0.01983275 seconds
    #  CPU time: 0.01977900 seconds
    solution2()
    # Result: 31875000
    #  Real time: 0.00870092 seconds
    #  CPU time: 0.00869300 seconds


if __name__ == "__main__":
    main()
