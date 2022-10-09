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

#make random module to generate the password
temp1 = random.sample(output1, length)
temp2 = random.sample(output2, length)

#join all characters together
password1 ="".join(temp1)
password2 ="".join(temp2)

print('\nPassword Generated Successfully.')
print('> Simple: '+password1)
print('> Strong: '+password2)