def get_largest_prime_factor(n):
    largest_prime = 0
    i = 2

    while i*i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 1

    if n > 1:
        largest_prime = n

    return largest_prime

def main():
    number = 600851475143
    print(get_largest_prime_factor(number)) # 6857

if __name__ == "__main__":
    main()
