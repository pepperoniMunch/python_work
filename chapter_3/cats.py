cats = ['callisto', 'phoebe', 'kane', 'jucint']

message = f"Here are all my cats:\n{cats[0]}\n{cats[1]}\n{cats[2]}\n{cats[3]}"

print(f"{message}\n")

print("And here are their names capitalized:")

print(cats[0].title())
print(cats[1].title())
print(cats[2].title())
print(cats[3].title())

# Print last item in the list with -1
print(cats[-1].upper())

# Methods can be done to list items
message_two = f"Here are all my cats:\n{cats[0].upper()}\n{cats[1].lower()}\n{cats[2].title()}\n{cats[3]}"

print(message_two)
