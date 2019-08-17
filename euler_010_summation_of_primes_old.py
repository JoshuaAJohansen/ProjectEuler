# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from modules.is_prime import is_prime
from modules.sieve_of_eratosthenes import primes_sieve
from modules.utils import thyme


# decorator to calculate time function takes to run.
@thyme
def sum_of_primes():
    sum_ = 2
    for x in range(3, 2000000, 2):
        if is_prime(x):
            sum_ += x
    return sum_


@thyme
def sieve_sum(n):
    return sum(primes_sieve(n))


# Function sum_of_primes took 5.767881 seconds.
# 142913828922
print(sum_of_primes())
# Function sieve_sum took 1.401701 seconds.
# 142913828922
print(sieve_sum(2000000))

