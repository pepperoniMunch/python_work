age = 25
admission_under_four = 0
admission_under_eighteen = 25
admission_over_eighteen = 40

if age < 4:
    print(f"You can enter for ${admission_under_four}.")
elif (age >= 4) and (age < 18):
    print(f"You can enter for ${admission_under_eighteen}.")
else:
    print(f"You can enter for ${admission_over_eighteen}.")

# A more concise take

age = 17

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 18:
    price = 40

print(f"Yoe can enter for ${price}.")