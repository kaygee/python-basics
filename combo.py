# Create a function named combo() that takes two iterables and returns a list of
# tuples. Each tuple should hold the first item in each list, then the second set,
# then the third, and so on. Assume the iterables will be the same length.
#
# combo(['swallow', 'snake', 'parrot'], 'abc')
# Output:
# [('swallow', 'a'), ('snake', 'b'), ('parrot', 'c')]
# If you use list.append(), you'll want to pass it a tuple of new values.
# Using enumerate() here can save you a variable or two.

def combo(first_iterable, second_iterable):
    list_of_tuples = []
    for first_item, second_item in zip(first_iterable, second_iterable):
        list_of_tuples.append((first_item, second_item))
    return list_of_tuples

first_iterable = ['swallow', 'snake', 'parrot']
second_iterable = 'abc'

print(combo(first_iterable, second_iterable))
