destinations = [
    'tokyo',
    'vienna',
    'delhi',
    'johannesburg',
    'reykjavik']

print(destinations)

# Using sorted() to print list in alphabetical order. Note this does not alter the list.
print(sorted(destinations))

# Proof that list order is unchanged
print(destinations)

# Using reverse sorted
print(sorted(destinations, reverse = True))

# Proof that list is unchanged
print(destinations)

# Reversing the lists
destinations.reverse()
print(destinations)

# Reversing the list to bring it back to original
destinations.reverse()
print(destinations)

# Sorting the list alphabetically
destinations.sort()
print(destinations)

# Sorting the list reverse alphabetically
destinations.sort(reverse = True)
print(destinations)

