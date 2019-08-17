# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


def compute():
    num = 2**1000
    print(sum_digits(num))


def sum_digits(n):
    sum_ = 0
    while n:
        sum_ += n % 10
        n //= 10
    return sum_


compute()  # 1366

