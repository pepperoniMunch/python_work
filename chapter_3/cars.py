cars = ['bmw', 'zzz', 'audi', 'toyota', 'subaru']

# cars.sort will permanently sort all list items
cars.sort()
print(cars)

# Adding the argument reverse = True sorts the list in reverse
cars.sort(reverse=True)
print(cars)

# cars.sorted() will temporarily sort the cars
print(sorted(cars))

# The list structure will be unaffected
print(cars)