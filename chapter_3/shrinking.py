# Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'gary snyder')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.\n")

print(f"Oh no! My table is now too small. I can only invite 2 of you now.\n")

name = guests.pop()
print(f"Sorry, {name.title()}, you can't come to dinner.\n")

name = guests.pop()
print(f"Sorry, {name.title()}, you can't come to dinner.\n")

name = guests.pop()
print(f"Sorry, {name.title()}, you can't come to dinner.\n")

name = guests.pop()
print(f"Sorry, {name.title()}, you can't come to dinner.\n")

print(guests)

print(f"Hey {guests[0]}, you're still invited!")
print(f"Hey {guests[1]}, you're still invited!\n")

print(guests)

del guests[0]
del guests[0]

print(guests)
