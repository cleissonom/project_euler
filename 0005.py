# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?

import math
import time


def loop_solution():
    i = 2520
    while True:
        if all([i % num == 0 for num in range(1, 20 + 1)]):
            return i
        i += 20


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def gcd_solution():
    lcm_result = 1
    for i in range(11, 20 + 1):
        lcm_result = lcm(lcm_result, i)

    return lcm_result


# Test cases
def measure_time(func):
    t1 = time.perf_counter(), time.process_time()
    print("Result:", func())
    t2 = time.perf_counter(), time.process_time()
    return f" Real time: {t2[0] - t1[0]:.8f} seconds\n CPU time: {t2[1] - t1[1]:.8f} seconds"


def main():
    print(measure_time(loop_solution))
    # Result: 232792560
    #  Real time: 15.62605388 seconds
    #  CPU time: 15.09860800 seconds

    print(measure_time(gcd_solution))
    # Result: 232792560
    #  Real time: 0.00004892 seconds
    #  CPU time: 0.00004800 seconds


if __name__ == "__main__":
    main()
