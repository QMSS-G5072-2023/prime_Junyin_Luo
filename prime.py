"""Main module."""
import math

"""
This is a Python function example that determines if a number is prime.

Purpose:
The purpose of this function is to check if a given number is prime.

Parameters:
n : int
    An integer that you want to check if it's a prime number.

Returns:
bool
    Returns True if n is a prime number, otherwise returns False.

Implementation Details:
1. If the number n is less than or equal to 1, it directly returns False.
2. Uses a for loop starting from 2 up to the square root of the number n.
3. During the loop, if n is divisible by any number (i.e., remainder is 0), it returns False.
4. If none of the above conditions are met, meaning n is not divisible by any number from 2 up to its square root, then n is a prime number, and it returns True.

Examples:
>>> is_prime(2)
True
>>> is_prime(4)
False
>>> is_prime(17)
True
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True