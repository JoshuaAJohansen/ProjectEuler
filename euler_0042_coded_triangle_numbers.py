from math import sqrt


def sum_characters(word):
    return sum(ord(char) - (ord('A') - 1) for char in list(word))


def is_triangle_word(x):
    calculation = ((sqrt(1 + 8 * x) -1) / 2)
    return float(calculation).is_integer()


def count_triangle_words():
    count = 0
    with open('./data/euler_0042/p042_words.txt', 'r') as file:
        words = file.read().replace('"', '').split(',')
        for word in words:
            if is_triangle_word(sum_characters(word)):
                count += 1

    return count


print("Solution: {}".format(count_triangle_words()))