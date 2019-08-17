from modules.utils import thyme

'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''


def score_name(word):
    return sum(ord(char) - (ord('A') - 1) for char in list(word))


@thyme
def compute():
    with open('./data/euler_0022/names.txt', 'r') as file:
        parsed_output = file.read().replace('"', '').split(',')
        sum_name_scores = 0
        for index, name in enumerate(sorted(parsed_output), start=1):
            sum_name_scores += score_name(name) * index
    return sum_name_scores


# Function compute took 0.01397 seconds.
# 871198282
print(compute())
