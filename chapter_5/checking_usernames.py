

current_users = ['Amanda', 'mandy', 'mando', 'mandi', 'mandybuzz', 'admin']
new_users = ['Mandy', 'jucint', 'bumbum', 'plumbum', 'alcatrazz', 'Mando']

current_users_lower = [user.lower() for user in current_users]
new_users_lower = [user.lower() for user in new_users]

print(current_users_lower)
print(new_users_lower)

for user in new_users_lower:
    if user in current_users_lower:
        print(f"Sorry, {user} is taken! Please choose a different username.")
    else:
        print(f"Thank you. This {user} is available.")
