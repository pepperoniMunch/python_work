guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

total_guests = len(guests)
print(f"I am inviting {total_guests} people to dinner!")

# Demonstrating index out of range
print(guests[4])