usernames = ['sufian']

if usernames:

    for username in usernames:
        if username == 'admin':
            print(f"Welcome back, {username.title()}! Would you like to see a status report?")
        else:
            print(f"Hello {username.title()}! Thank you for logging in again.")

else:
    print("We need to find some users!")