# Create a function named word_count() that takes a string.
# Return a dictionary with each word in the string as the key and the number of
# times it appears as the value.
#
# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

def word_count(sentence):
    words = sentence.split()
    word_count = dict()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

empty = ""
repeating = "the the the the the the the the"
one_repeat = "the the"
sentence = "The quick brown fox jumped over the lazy brown dog"
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(word_count(empty))
print(word_count(repeating))
print(word_count(one_repeat))
print(word_count(sentence))
print(word_count(lorem))
