# import libraries
import random
import string

# define lists
uppercase_letters_list = list(string.ascii_uppercase)
lowercase_letters_list = list(string.ascii_lowercase)
numbers_list = list(string.digits)
symbols_list = list(string.punctuation)

# take input from user
no_of_char = input('Please enter the number of charachters you want in your password: ')

# check if the input is a number
while True:
    try:
        no_of_char = int(no_of_char)
        if no_of_char < 6:
            print('Password must be at least 6 characters long')
            no_of_char = input('Please enter the number of charachters you want in your password: ')
        else:
            break
    except:
        print('Please enter a number')
        no_of_char = input('Please enter the number of charachters you want in your password: ')

# allocate proportions
uppercase_letters = int(no_of_char * 0.3)
lowercase_letters = int(no_of_char * 0.3)
numbers = int(no_of_char * 0.2)
symbols = no_of_char - uppercase_letters - lowercase_letters - numbers

password = []

# shuffle the lists
random.shuffle(uppercase_letters_list)
random.shuffle(lowercase_letters_list)
random.shuffle(numbers_list)
random.shuffle(symbols_list)

# generate password
for i in range(uppercase_letters):
    password.append(uppercase_letters_list[i])

for i in range(lowercase_letters):
    password.append(lowercase_letters_list[i])

for i in range(numbers):
    password.append(numbers_list[i])

for i in range(symbols):
    password.append(symbols_list[i])

# shuffle the password
random.shuffle(password)

# print the password
final_password = ''.join(password)
print(final_password)

input('Press any key to exit')