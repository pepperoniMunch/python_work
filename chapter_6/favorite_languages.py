favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}!")
print("\n")

# Alternative solution using looping

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite programming language is {language.title()}!")