'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

def sum_of_squares(n):
    sum_ = 0
    for x in range(1, n+1):
        sum_ += x * x
    return sum_

def square_of_sum(n): 
    sum_ = 0
    for x in range(1, n+1):
        sum_ += x
    square_of_sum = sum_ * sum_
    return sum_ * sum_

difference = square_of_sum(100) - sum_of_squares(100)

print('Solution: {}'.format(difference))