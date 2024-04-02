# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time


def loop_solution(n=100):
    sum_of_squares = 0
    for num in range(1, n + 1):
        sum_of_squares += pow(num, 2)

    return pow((n * (1 + 100) / 2), 2) - sum_of_squares


def math_solution(n=100):
    sum = pow((n * (1 + 100) / 2), 2)
    sum_square = (2 * n + 1) * (n + 1) * n / 6
    return sum - sum_square


# Test cases
def measure_time(func):
    t1 = time.perf_counter(), time.process_time()
    print("Result:", func())
    t2 = time.perf_counter(), time.process_time()
    return f" Real time: {t2[0] - t1[0]:.8f} seconds\n CPU time: {t2[1] - t1[1]:.8f} seconds"


def main():
    print(measure_time(loop_solution))
    # Result: 25164150.0
    #  Real time: 0.00026950 seconds
    #  CPU time: 0.00008300 seconds
    print(measure_time(math_solution))
    # Result: 25164150.0
    #  Real time: 0.00000408 seconds
    #  CPU time: 0.00000400 seconds


if __name__ == "__main__":
    main()
