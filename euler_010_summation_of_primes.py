# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


from modules.is_prime import is_prime
from modules.sieve_of_eratosthenes import primes_sieve
from modules.utils import thyme


@thyme
def sum_of_primes():
    _sum = 2
    for x in range(3, 2000000, 2):
        if is_prime(x):
            _sum += x
    return _sum


@thyme
def sieve_sum(n):
    return sum(primes_sieve(n))


sum_of_primes()
sieve_sum(2000000)
