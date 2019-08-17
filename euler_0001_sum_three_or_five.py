'''
Problem 1
Add all the natural numbers below one thousand that are multiples of 3 or 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

import unittest


def bruteforce():
    sum_ = 0
    max_number = 1000

    for x in range(1, max_number):
        if x % 3 == 0 or x % 5 == 0:
            sum_ = sum_ + x
    return (sum_)
    
def optimized():
    sum_ = 0
    max_number = 1000
    for x in range(3,max_number, 3):
        sum_ += x
    for x in range(5,max_number, 5):
        sum_ += x
    for x in range(15,max_number, 15):
        sum_ -= x
    return sum_

optimized_solution = optimized()
bruteforce_solution = bruteforce()

print ('Bruteforce:{}'.format(bruteforce_solution))
print ('Optimized:{}'.format(optimized_solution))


class Test_Euler_001(unittest.TestCase):
    def test_bruteforce(self):
        self.assertEqual(233168, bruteforce())

    def test_optimized(self):
        self.assertEqual(233168, optimized())

unittest.main()