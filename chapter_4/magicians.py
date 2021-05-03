magicians = ['alice', 'david', 'carolina']

# Demonstrating a for loop to print all magicians in list; follow this structure: for item in list_of_items
for magician in magicians:
    print(magician.title())

# Loops can do many things! Here we use loops to send each magician a message.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"We're looking forward to your next trick, {magician.title()}!\n")

print("Thank you, everyone, for the magic.")
