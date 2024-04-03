# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from helpers import measure_time


@measure_time
def get_largest_prime_factor(n):
    largest_prime = 0
    i = 2

    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 1

    if n > 1:
        largest_prime = n

    return largest_prime


def main():
    get_largest_prime_factor(600851475143)
    # Result: 6857
    #  Real time: 0.00015492 seconds
    #  CPU time: 0.00015300 seconds


if __name__ == "__main__":
    main()
