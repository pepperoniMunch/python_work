# Define list
my_foods = ['pizza', 'falafel', 'carrot cake', 'roti', 'shawarma', 'mcdouble']
print(my_foods)
print("\n")

print("My three favourite foods are:\n")
# Access first three list items by looping through a slice
for foods in my_foods[0:3]:
    print(foods.title())

print("Some of my lesser favourite foods are:\n")
# Access three items from the middle of the list
for foods in my_foods[3:6]:
    print(foods.title())

print("Some of my least favourite foods are:\n")
# Access the final three items from the list
for foods in my_foods[-3:]:
    print(foods.title())
