# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

# Find the largest palindrome made from the product of two 3-digit numbers.

from helpers import measure_time


# Solution using strings
def is_palindrome_str(n):
    return str(n) == str(n)[::-1]


@measure_time
def loop_solution():
    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if is_palindrome_str(product):
                largest_palindrome = product

    return largest_palindrome


# Since we are looking for a maximal product, we will assume that it is a 6-digit one. Observe that:

# abccba=100000×a+10000×b+1000×c+100×c+10×b+a
#       =100001×a+10010×b+1100×c
#       =11×(9091×a+910×b+100×c)

# Since 11|x × y and 11 is prime then 11|x or 11|y. Without loss of generality, assume that 11|y.
# To solve this problem search through all 3-digit numbers x,y ∈ ℕ where 11|y. Then, identify all palindromic products x×y. Find the maximum such x×y.
# Solved with help of: https://euler.beerbaronbill.com/en/latest/solutions/4.html


def is_palindrome_math(n):
    temp = n
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp //= 10

    return True if rev == n else False


@measure_time
def math_solution():
    answer = 0
    for x in range(100, 1000):
        for y in range(110, 1000, 11):
            if is_palindrome_math(x * y):
                answer = max(answer, x * y)
    return answer


def main():
    loop_solution()
    # Result: 906609
    #  Real time: 0.00209554 seconds
    #  CPU time: 0.00209500 seconds
    math_solution()
    # Result: 906609
    #  Real time: 0.04149167 seconds
    #  CPU time: 0.04139400 seconds


if __name__ == "__main__":
    main()
