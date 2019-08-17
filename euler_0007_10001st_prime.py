'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from modules.is_prime import is_prime


def nth_prime(n):
	prime_ctr = 0
	num = 1
	while (prime_ctr < n):
		num += 1
		if is_prime(num):
			print('prime: {}'.format(num))
			prime_ctr += 1
	return num


solution = nth_prime(10001)
print('Solution: {}'.format(solution)) #104743