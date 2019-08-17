'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import unittest

from math import floor, sqrt
from modules.is_prime import is_prime


def largest_prime_factor(n):
    UPPERBOUND = floor(sqrt(n))

    for x in range(UPPERBOUND,2,-1):
        if n % x == 0:
            if is_prime(x):
                return x

solution = largest_prime_factor(600851475143)
print('Solution: {}'.format(solution))

class Test_Euler_001(unittest.TestCase):
    def test_sample_solution(self):
        self.assertEqual(29, largest_prime_factor(13195))

    def test_largest_prime_factor(self):
        self.assertEqual(6857, largest_prime_factor(600851475143))


unittest.main()