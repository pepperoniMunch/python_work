move_option_one = 'may 31st'
move_option_two = 'june 30th'

metcap_approval = False
amanda_job = True
sufian_school = True

if metcap_approval == False:
    print(f"You have to move on {move_option_two.upper()}.")
    if amanda_job == True and sufian_school == True:
        print(f"You must move to Waterloo.")
    elif amanda_job == True and sufian_school == False:
        print(f"You must move to where Amanda's job is.")
    else:
        print(f"You must move to Sufian's parents' abode.")

if metcap_approval == True:
    if amanda_job == True:
        print(f"You must move to where Amanda's job is.")
    else:
        print(f"You must move on {move_option_one.upper()} to Sufian's parents' abode.")


