# https://github.com/MithunWijayasiri/PasswordsGenerator-python

from operator import length_hint
import random
import string

print('Hi, Welcome to Passwords Generator!')

length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


output1 = lower+upper+num
output2 = lower+upper+num+symbols

if length < 1:
    print('Invalid Input!')
    
else:
    #make a random module to generate the password
    temp1 = random.sample(output1, length)
    temp2 = random.sample(output2, length)
    
    #join all characters together
    password1 ="".join(temp1)
    password2 ="".join(temp2)
    
    if length < 8:
        print('\nPassword generated but not recommended to use this password.')
        print('Input a number Greater Than 8.')
        print('\n> Output 1: '+password1)
        print('> Output 2: '+password2)
        
    else:
        print('\nPassword Generated Successfully.')
        print('> Simple: '+password1)
        print('> Strong: '+password2)