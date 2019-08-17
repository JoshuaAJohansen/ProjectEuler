'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
''' 

def is_pythagorean_triplet(a, b, c):
	# https://stackoverflow.com/questions/20969773/exponentials-in-python-x-y-vs-math-powx-y#20970087
    return a ** 2 + b ** 2 == c ** 2

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        if is_pythagorean_triplet(a, b, c):
            print(a, b, c)
            print("Product: {}".format(a * b * c))
            exit(0)

# def is_pythagorean_triplet(a, b, c):
# 	result = (c - a) * (c - b) / 2
# 	print(result)
# 	# if (a + b + c == 1000):
# 	# 	return True

# print(is_pythagorean_triplet(300, 300, 400))

# def triplet(a, b, c):
# 	if (expresssion):
# 			statement

# 	return true;

# def bruteforce():
# 	print(pow(2, 2))
#     # return product
    
# def optimized():
#     return product

# optimized_solution = optimized()
# bruteforce_solution = bruteforce()

# print ('Bruteforce:{}'.format(bruteforce_solution))
# print ('Optimized:{}'.format(optimized_solution))