# Demo of a list comprehension
my_pizzas = ['pepperoni', 'cheese', 'supreme', 'deluxe', 'veggie', 'hawaiian']

# Copy list
friend_pizzas = my_pizzas[:]

print(f"My favourite pizzas are:")
print(my_pizzas)

print(f"My friends favourite pizzas are:")
print(friend_pizzas)

# Add new pizzas to each list
my_pizzas.append('margherita')
friend_pizzas.append('cheeseburger')

# Prove that two separate lists exist
print(my_pizzas)
print(friend_pizzas)

# Use for loops to do the above task
print("\n")
print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())