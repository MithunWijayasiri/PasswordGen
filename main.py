# https://github.com/MithunWijayasiri/PasswordGenerator-1

from operator import length_hint
import random
import string

print('Hi, This is Simple Password Generator!')

length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

output = lower+upper+num+symbols

#make random module to generate the password
temp = random.sample(output, length)

#join all characters together
password ="".join(temp)
print(password)

print('Password Generated Successfully')