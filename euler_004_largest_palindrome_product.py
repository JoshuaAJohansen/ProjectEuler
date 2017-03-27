'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from modules.string import is_palindrome
import unittest

def largest_palindrome_product():
  maxPalindrome = 0;
  for x in range(100,999):
    for y in range(100,999):
      product = x * y
      if is_palindrome(product) and product > maxPalindrome:
        maxPalindrome = product
  return(maxPalindrome)

print('Solution: {}'.format(largest_palindrome_product()))

class Test_Euler_004(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(906609, largest_palindrome_product())

unittest.main()