# Define list
my_foods = ['pizza', 'falafel', 'carrot cake']

# Copy list by not assigning slice indices
friend_foods = my_foods[:]

print("My favourite foods are:\n")
for foods in my_foods:
    print(foods.title())

print("\nMy friend's favourite foods are:\n")
for foods in friend_foods:
    print(foods.title())