import math


def find_primes(numbers):


    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]



ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = find_primes(ls)

print("Input Numbers:", ls)
print("Prime Numbers:", prime_numbers)



