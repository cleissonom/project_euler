# Travel the Fibonacci sequence and sum all the even numbers

def fibonacci_sum_even(limit):
    # a is the current number, b is the next number
    a, b = 1, 1
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b
    return even_sum

limit = 4000000
result = fibonacci_sum_even(limit)
print(result)
