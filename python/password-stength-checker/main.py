import string

password = input("Enter a password: ")

length = False
uppercase = False
lowercase = False
number = False
special = False

if len(password) >= 8:
    length = True

for character in password:

    if character.isupper():
        uppercase = True

    if character.islower():
        lowercase = True

    if character.isdigit():
        number = True

    if character in string.punctuation:
        special = True

score = 0

if length:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1

if number:
    score += 1

if special:
    score += 1

print("\nPassword Analysis")

if score == 5:
    print("Very Strong Password")
elif score == 4:
    print("Strong Password")
elif score == 3:
    print("Medium Password")
elif score == 2:
    print("Weak Password")
else:
    print("Very Weak Password")
