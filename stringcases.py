# Create a function named stringcases that takes a string and returns a tuple
# of four versions of the string: uppercased, lowercased, titlecased (where every
# word's first letter is capitalized), and a reversed version of the string.
#
# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?
def stringcases(input):
    return input.upper(), input.lower(), input.title(), input[::-1]

empty = ""
single = "k"
multiple = "kevin"

print(stringcases(empty))
print(stringcases(single))
print(stringcases(multiple))
