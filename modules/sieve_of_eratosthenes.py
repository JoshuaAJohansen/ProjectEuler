def primes_sieve(limit):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    limit+= 1
    not_prime = set()
    primes = []

    for i in range(2, limit):
        if i in not_prime:
            continue
        for f in range(i * 2, limit, i):
            not_prime.add(f)

        primes.append(i)

    return primes


# pytest sieve_of_eratosthenes.py
def test_sieve():
    actual  = (primes_sieve(19))
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    assert all([a == b for a, b in zip(actual, expected)])
