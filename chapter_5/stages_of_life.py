# Define variable age
age = 999

# Write an if-elif-else chain that determines a person's stage of life
if age < 2:
    print("You're a baby.")
elif 2 < age < 4:
    print("You're a toddler.")
elif 4 < age < 13:
    print("You're a kid.")
elif 13 < age < 20:
    print("You're a teenager.")
elif 20 < age < 65:
    print("You're an adult.")
elif age > 65:
    print("You're an elder.")
elif age > 150:
    print("I think you might be a Sith lord!")
