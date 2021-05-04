banned_users = ['andrew', 'carolina', 'david']
user = 'sufian'

if user not in banned_users:
    print(f"Welcome to the website, {user.title()}!")
else:
    print("You are banned!")