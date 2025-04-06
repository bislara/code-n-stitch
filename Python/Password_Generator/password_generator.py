import string
import random

length = int(input("Enter length of your password:\n"))

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
UPPER_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 
              'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 
              'T', 'U', 'V', 'W', 'X', 'Y','Z']
LOWER_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
              'z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', 
           '|', '~', '>', '*', '(', ')', '<']

#ALl the valid characters that can be used in a password
VALID_CHARS = DIGITS+UPPER_CASE+LOWER_CASE+SYMBOLS

#Adding atleast 1 character of all types of valid characters
password_temp = random.choice(DIGITS)+ random.choice(UPPER_CASE)+ random.choice(LOWER_CASE)+ random.choice(SYMBOLS)

if(length<8):
    print("Password must be atleast 8 character long")
else:
    for i in range(length-4):

        #get the rest of the valid characters randomly
        password_temp += random.choice(VALID_CHARS) 

        #Convert password_temp into a list and shuffle it
        password_list = list(password_temp)
        random.shuffle(password_list)
    
    #Convert yhe shuffled password_list back to password string
    password = ""
    for x in password_list:
        password+=x

    print(password)