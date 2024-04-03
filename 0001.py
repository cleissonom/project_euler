# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000


from helpers import measure_time


@measure_time
def solution1(limit=1000):
    def sum_multiple(n):
        p = (limit - 1) // n
        return n * p * (p + 1) // 2

    return sum_multiple(3) + sum_multiple(5) - sum_multiple(15)


@measure_time
def solution2(limit=1000):
    return (
        (3 * ((limit - 1) // 3) * (((limit - 1) // 3) + 1) // 2)
        + (5 * ((limit - 1) // 5) * (((limit - 1) // 5) + 1) // 2)
        - (15 * ((limit - 1) // 15) * (((limit - 1) // 15) + 1) // 2)
    )


@measure_time
def solution3(limit=1000):
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


def main():
    test_limit = 999_888_777
    solution1(test_limit)
    # Result: 233281432053140793
    #   Real time: 0.00002625 seconds
    #   CPU time: 0.00002500 seconds

    solution2(test_limit)
    # Result: 233281432053140793
    #   Real time: 0.00001533 seconds
    #   CPU time: 0.00001500 seconds

    solution3(test_limit)
    # Result: 233281432053140793
    #   Real time: 72.78611975 seconds
    #   CPU time: 72.53000900 seconds


if __name__ == "__main__":
    main()
