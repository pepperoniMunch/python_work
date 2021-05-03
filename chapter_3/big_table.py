# Define list of guests to be invited
guests = ['sufian fitzgerald-malik', 'ken chatoor', 'robert smith', 'rob ford']

# Invite first round of guests
print(f"{guests[0].title()}, would you join me for dinner on May 24th?\n")
print(f"{guests[1].title()}, would you join me for dinner on May 24th?\n")
print(f"{guests[2].title()}, would you join me for dinner on May 24th?\n")
print(f"{guests[3].title()}, would you join me for dinner on May 24th?\n")

# Whoops, Rob Ford can't make it!
unavailable = guests.pop(-1).title()
print(f"{unavailable} can't make it!\n")

# Adding Alexandro to the guest list
guests.append('alexandro kirk')
print(guests)

# Inviting Alexandro
new_invite = guests[-1]
print(f"{new_invite.title()}, will you join us since {unavailable} can't make it?\n")

# Telling the friends about my new dinner table :)
print("Great news! I found a bigger table and will invite more folks to dinner.")

# Using insert feature to conjure the dead
guests.insert(0, 'joseph stalin')
print(guests)

guests.insert(0, 'nelson mandela')
guests.insert(-1, 'jennifer lopez')
print(guests)

name = guests[0]
print(f"Hey {name.title()}! Would you join me for dinner?")


