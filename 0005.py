# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?

import math

from helpers import measure_time


@measure_time
def loop_solution(n=20):
    i = n
    while True:
        if all([i % num == 0 for num in range(1, n + 1)]):
            return i
        i += n


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


@measure_time
def gcd_solution(n=20):
    lcm_result = 1
    for i in range(2, n + 1):
        lcm_result = lcm(lcm_result, i)

    return lcm_result


def main():
    loop_solution()
    # Result: 232792560
    #  Real time: 15.03269071 seconds
    #  CPU time: 14.69493800 seconds
    gcd_solution()
    # Result: 232792560
    #  Real time: 0.00005804 seconds
    #  CPU time: 0.00005800 seconds


if __name__ == "__main__":
    main()
