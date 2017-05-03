'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def is_multiple(n, a, b):
    for x in range(a,b):
        if n%x != 0:
            return False
    return True

smallest = 20
while is_multiple(smallest,11,20) == False:
    print(smallest)
    smallest += 20

print('Solution: {}'.format(smallest))
