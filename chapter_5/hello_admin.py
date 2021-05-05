usernames = ['amanda', 'mandy', 'mando', 'mandi', 'mandybuzz', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"Welcome back, {username.title()}! Would you like to see a status report?")
    else:
        print(f"Hello {username.title()}! Thank you for logging in again.")