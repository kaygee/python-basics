def members(dictionary, keys):
    count = 0
    for key in keys:
        if key in dictionary.keys():
            count += 1
    return count

dictionary = {'jack': 4098, 'sape': 4139}
keys = ['jack']
keys_2 = ['bob', 'kevin']
keys_2 = ['bob', 'kevin']
keys_3 = ['jack', 'sape']

# zero
print(members(dictionary, keys))
# one
print(members(dictionary, keys_2))
#many
print(members(dictionary, keys_3))
