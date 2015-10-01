import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

print(re.match(r'Love', data))
print(re.search(r'Kenneth', data))

# \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character.
# \W - is the opposite and matches anything that isn't an Unicode word character.
# \s - matches whitespace, so spaces, tabs, newlines, etc.
# \S - matches everything that isn't whitespace.
# \d - is how we match any number from 0 to 9
# \D - matches anything that isn't a number.
# \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
# \B - matches things that aren't the edges of a word.

print(re.search(r'\d{3}-\d{4}', data))
print(re.search(r'\(?\d{3}\)? \d{3}-\d{4}', data))
# ? means optional
# \s means space
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

# Now, write a function named numbers() that takes two arguments: a count as an integer
# and a string. Return an re.search for exactly count numbers in the string.
# Remember, you can multiply strings and integers to create your pattern.
# For example: r"\w" * 5 would create r"\w\w\w\w\w".

def first_number(argument):
    return re.search(r'\d', argument)

def numbers(count, string):
    return re.search(r'\d' * count, string)

# \w{3} - matches any three word characters in a row.
# \w{,3} - matches 0, 1, 2, or 3 word characters in a row.
# \w{3,} - matches 3 or more word characters in a row. There's no upper limit.
# \w{3, 5} - matches 3, 4, or 5 word characters in a row.
# \w? - matches 0 or 1 word characters.
# \w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
# \w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
# .findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.

print(re.search(r'\w+, \w+', data))
print(re.findall(r'\w*, \w+', data))

# Create a function named phone_numbers that takes a string and returns all of
# the phone numbers in the string using re.findall(). The phone numbers will
# all be in the format 555-555-5555.
def phone_numbers(string):
    return re.findall(r'\d{3}-\d{3}-\d{4}', string)

# Create a function named find_words that takes a count and a string.
# Return a list of all of the words in the string that are count word characters long or longer.
# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']
search_string = "dog, cat, baby, balloon, me"

def find_words(count, search_string):
    regex = r"\w{" + str(count) + ",}"
    return re.findall(regex, search_string)

print("Finding words...")
print(find_words(4, search_string))

# [abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
# [a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
# [0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.

print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

print(re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))

# Create a function named find_emails that takes a string. Return a list of all
# of the email addresses in the string.
# Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']
emails = "kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk"
def find_emails(search_string):
    return re.findall(r'[-\w\d+.]+@[-\w\d.]+', search_string)

print("Finding Hillary Clinton email addresses...")
print(find_emails(emails))

# negative set
print(re.findall(r'''
    \b@[-\w\d.]*    #First a word boundary, an @, and then any number of characters
    [^gov\t]+       # Ignore 1+ instances of the letters g o v and a tab.
    \b              # Match another word boundary.
''', data, re.VERBOSE | re.IGNORECASE))

print("Names and where they work.")
print(re.findall(r'''
    \b[-\w]*, # Find a word boundary, 1+ hyphens or characters, and a comma
    \s        # Find 1 whitespace
    [-\w ]+    # 1+ hyphens and characters and explicit spaces
    [^\t\n]   # Ignore tabs and newlines
''', data, re.VERBOSE))

number_search_string = '1234567890'
good_numbers = re.findall(r'[^567]' ,number_search_string)
print("The good numbers are: {}".format(good_numbers))


# ([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
# (?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').
# .groups() - method to show all of the groups on a Match object.
# re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.
# ^ - specifies, in a pattern, the beginning of the string.
# $ - specifies, in a pattern, the end of the string.

print("Finding it all using groups!")
print(re.findall(r'''
    ([-\w ]+,\s[-\w ]+)\t           # Last and First Names
    ([-\w\d.+]+@[-\w\d.]+)\t        # email
    (\(?\d{3}\)?-?\s?\d{3}-\d{4})\t # Phone
    ([\w\s]+,\s[\w\s]+)\t           # Job and Company
    (@[\w\d]+)                      # Twitter
''', data, re.VERBOSE | re.IGNORECASE))

# Create a variable names that is an re.match() against string. The pattern
# should provide two groups, one for a last name match and one for a first name
# match. The name parts are separated by a comma and a space.

name_string = 'Perotto, Pier Giorgio'
name_string_match = re.match(r'''
    ([\w]+),\s
    ([\w\s]+)
''', name_string, re.IGNORECASE | re.VERBOSE)

print("Names string match.")
print(name_string_match)

# Create a new variable named contacts that is an re.search() where the pattern
# catches the email address and phone number from string. Name the email pattern
# email and the phone number pattern phone. The comma and spaces * should not*
# be part of the groups.

contacts_list = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+),\s
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})
''', contacts_list, re.IGNORECASE | re.VERBOSE)

print("Contacts!")
print("Name [{}]".format(contacts.group(1)))
print("Phone number [{}]".format(contacts.group(2)))

print("compiled contacts and subgroups")

compiled_contacts = re.compile(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+)
    ,\s
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})
''', re.IGNORECASE | re.VERBOSE)

for match in compiled_contacts.finditer(contacts_list):
    print("area code [{phone}]".format(**match.groupdict()))

# Great! Now, make a new variable, twitters that is an re.search() where the
# pattern catches the Twitter handle for a person. Remember to mark it as being
# at the end of the string. You'll also want to use the re.MULTILINE flag.

twitters = re.search(r'''
    (?P<twitters>@[\w\d]+)$
''', contacts_list, re.VERBOSE | re.MULTILINE)

print("Twitters")
print(twitters)

# re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
# .groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
# re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
# .group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.

compiled_regex = re.compile(r'''
    (?P<twitters>@[\w\d]+)$
''', re.VERBOSE | re.MULTILINE)

print(re.search(compiled_regex, contacts_list).groupdict())

for match in compiled_regex.finditer(contacts_list):
    print(match.group('twitters'))

# Create a variable named players that is an re.search() or re.match() to capture
# three groups: last_name, first_name, and score. It should include re.MULTILINE.

players_data = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

print("Players...")

players = re.search(r'''
    (?P<last_name>[-\w ]*)
    ,\s
    (?P<first_name>[-\w ]*)
    :\s
    (?P<score>[\d]*)
''', players_data, re.MULTILINE | re.VERBOSE |re.IGNORECASE)

print(players)

class Player:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


players_compiled = re.compile(r'''
    (?P<last_name>[-\w ]*)
    ,\s
    (?P<first_name>[-\w ]*)
    :\s
    (?P<score>[\d]*)
''', re.MULTILINE | re.VERBOSE |re.IGNORECASE)

print(re.search(players_compiled, players_data).groupdict())
