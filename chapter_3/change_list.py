# Define list of guests to be invited
guests = ['sufian fitzgerald-malik', 'ken chatoor', 'robert smith', 'rob ford']

print(f"{guests[0].title()}, would you join me for dinner on May 24th?\n")
print(f"{guests[1].title()}, would you join me for dinner on May 24th?\n")
print(f"{guests[2].title()}, would you join me for dinner on May 24th?\n")
print(f"{guests[3].title()}, would you join me for dinner on May 24th?\n")

unavailable = guests.pop(-1).title()
print(f"{unavailable} can't make it!\n")

guests.append('alexandro kirk')
print(guests)

new_invite = guests[-1]
print(f"{new_invite.title()}, will you join us since {unavailable} can't make it?\n")


