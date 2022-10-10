# A random password generator I use daily as a script within Raycast.

import string
import random

letters = list(string.ascii_letters)
digits = list(string.digits)
special = list("!@#$%^&*()")                  # using top mac row - edit as needed by site
final_pwd = []

length_total = int(input("Please enter password character length: "))
letters_count = int(input("Please enter number of alphabets to use for password: "))
digits_count = int(input("Please enter number of digits to use for password: "))
special_count = int(input("Please enter number of special characters to use for password: "))

while letters_count + digits_count + special_count > length_total:
    change_required = int(input("""The character count is more than the total length requested.
    Type '1' to decrease alphabet count
    Type '2' to decrease digit count
    Type '3' to decrease special characters' count
    Your input: """))
    if change_required == 1:
        letters_count = length_total - (digits_count + special_count)
    elif change_required == 2:
        digits_count = length_total - (letters_count + special_count)
    elif change_required == 3:
        special_count = length_total - (letters_count + digits_count)
    else:
        print("The value entered is not '1', '2' or '3'. Please retry.")

while letters_count + digits_count + special_count < length_total:
    change_required = int(input("""The character count is less than the total length requested.
    Type '1' to increase alphabet count
    Type '2' to increase digit count
    Type '3' to increase special characters' count
    Your input: """))
    if change_required == 1:
        letters_count = length_total - (digits_count + special_count)
    elif change_required == 2:
        digits_count = length_total - (letters_count + special_count)
    elif change_required == 3:
        special_count = length_total - (letters_count + digits_count)
    else:
        print("The value entered is not '1', '2' or '3'. Please retry.")

random.shuffle(letters)                 # first randomization for the sake of it
random.shuffle(digits)                  # can shuffle all three at once using numpy or zip list
random.shuffle(special)

for item in range(letters_count):
    final_pwd.append(random.choice(letters))

for item in range(digits_count):
    final_pwd.append(random.choice(digits))

for item in range(special_count):
    final_pwd.append(random.choice(special))

random.shuffle(final_pwd)                # final randomization of selected characters
print("".join(final_pwd))                # list to string conversion using join
