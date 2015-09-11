# The first half of the string, rounded with round(), should be lowercased.
# The second half should be uppercased.
# E.g. "Treehouse" should come back as "treeHOUSE"
def sillycase(tosillify):
  halfway = round(len(tosillify)/2)
  return tosillify[:halfway].lower() + tosillify[halfway:].upper()

print(sillycase("Oklahoma"))
