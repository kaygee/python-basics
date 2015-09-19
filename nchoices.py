# Create a function named nchoices() that takes an iterable and an integer.
# The function should return a list of n random items from the iterable where n
# is the integer. Duplicates are allowed.
import random

def nchoices(iterable, n):
    list_of_random = []
    if len(iterable) > 0:
        while len(list_of_random) < n:
            index =random.randint(0, len(iterable)-1)
            list_of_random.append(iterable[index])
    return list_of_random


empty = []
single_list = ['a']
multiple_list = ['k', 'e', 'v', 'i', 'n']

print(nchoices(empty, 0))
print(nchoices(empty, 1))

print(nchoices(single_list, 0))
print(nchoices(single_list, 1))
print(nchoices(single_list, 10))


print(nchoices(multiple_list, 0))
print(nchoices(multiple_list, 1))
print(nchoices(multiple_list, 10))
