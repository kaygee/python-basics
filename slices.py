def first_4(iterable):
    return iterable[:4]

def odd_indexes(iterable):
    return iterable[1::+2]

def first_and_last_2(iterable):
    return iterable[:2] + iterable[-2:]


print(first_4("Oklahoma"))
print(odd_indexes("Oklahoma"))
print(first_and_last_2("Oklahoma"))
