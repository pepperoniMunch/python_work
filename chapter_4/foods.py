# Define list
my_foods = ['pizza', 'falafel', 'carrot cake']

# Copy list by not assigning slice indices
friend_foods = my_foods[:]

print("My favourite foods are:\n")
print(my_foods)

print("\nMy friend's favourite foods are:\n")
print(friend_foods)

# Prove two lists have been created

my_foods.append('roti')
print(my_foods)

friend_foods.append('donuts')
print(friend_foods)