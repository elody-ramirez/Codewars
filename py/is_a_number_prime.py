# Define a function that takes one integer argument and returns logical value
# true or false depending on if the integer is a prime.
#
# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.
#
# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given
# negative numbers as well (or 0).
# NOTE on performance: There are no fancy optimizations required, but still the
# most trivial solutions might time out. Numbers go up to 2^31 (or similar,
# depends on language version). Looping all the way up to n, or n/2, will be too
# slow.
# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */
import math

def is_prime(num):
    result = True
    if num > 2:
        top = int(math.sqrt(num)) + 1
        for i in range(2, top):
            print(num, i, num%i)
            if (num % i) == 0:
                result = False
    elif num < 2:
        result = False
    return result

# print(is_prime(0))    # False, "0  is not prime"
# print(is_prime(1))    # False, "1  is not prime"
# print(is_prime(2))    # True, "2  is prime"
# print(is_prime(73))   # True, "73 is prime"
# print(is_prime(75))   # False, "75 is not prime"
# print(is_prime(-1))   # False, "-1 is not prime"
#
# print(is_prime(3))    # True, "3  is prime"
# print(is_prime(5))    # True, "5  is prime"
# print(is_prime(7))    # True, "7  is prime"
# print(is_prime(41))   # True, "41 is prime"
# print(is_prime(5099)) # True, "5099 is prime"

print(is_prime(4))    # False, "4  is not prime"
print(is_prime(6))    # False, "6  is not prime"
print(is_prime(8))    # False, "8  is not prime"
print(is_prime(9))    # False, "9 is not prime"
# print(is_prime(45))   # False, "45 is not prime"
# print(is_prime(-5))   # False, "-5 is not prime"
# print(is_prime(-8))   # False, "-8 is not prime"
# print(is_prime(-41))  # False, "-41 is not prime"
