# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000


# Solution 0
def sum_of_multiples_of_3_or_5():
    def sum_multiple(n):
        p = (1000 - 1) // n
        return n * p * (p + 1) // 2

    return sum_multiple(3) + sum_multiple(5) - sum_multiple(15)


# Solution 1
def sum_of_multiples_of_3_or_5_below_1000(limit):
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


# Solution 2
def sum_all_multiples_of_3_or_5_below_1000():
    return (
        (3 * ((1000 - 1) // 3) * (((1000 - 1) // 3) + 1) // 2)
        + (5 * ((1000 - 1) // 5) * (((1000 - 1) // 5) + 1) // 2)
        - (15 * ((1000 - 1) // 15) * (((1000 - 1) // 15) + 1) // 2)
    )
