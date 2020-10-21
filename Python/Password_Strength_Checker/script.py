import re

digits, points, specs = 0, 0, 0
tooShort = False

pwd = input("Enter password: ")
pwdLen = len(pwd)

if (pwdLen < 8):                # check if password length is too short (less than 8 digits)
    tooShort = True

def isDigit(i):                     # check if character is a digit
    if (i >= '0' and i <= '9'):
        return True
    else:
        return False

for i in range (pwdLen):
    if pwd[i].islower() or pwd[i].isupper():       # check if character is an upper/lowercase alphabet
        points += 1
    elif isDigit(pwd[i]):
        digits += 1
    else:
        specs += 1                                  # if character isn't alphabet or digit, we'll assume it's a symbol/special character

if specs < 2:
    print("Password must contain at least 2 special characters!")
elif digits < 3:
    print("Password must contain at least 3 digits!")
elif tooShort:
    print("Password is too short! A good password is usually more than 8 characters.")
else:
    print("You have a vibranium-level password! Congrats!")