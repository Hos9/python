import random
import string
 
first=input("Enter your First name: ")
last=input("Enter your Last name: ")
num=int(input("Enter your Password length: "))
 
all_chars = string.ascii_letters+string.digits+string.punctuation
 
email = first+ '.' + last + '@gmail.com'
password = ''
 
for i in range(num):
   rand_char=random.choice(all_chars)
   password = password + rand_char
 
print("Your Gmail Id: "+ email)
print("Your Password: "+ password)

print('''
______________________________________
''')

import string
import random

fst = input('Your 1st name? ')
snd = input('Your 2nd name')
dig = int(input('pw length'))

a_c = string.ascii_letters + string.digits + string.punctuation

mail = fst + '.' + snd + '@gmail.com'
pw = ''

for i in range(dig):
  r_c = random.choice(a_c)
  pw = pw + r_c
 
print(f'Email: {mail}')
print(f'new pw: {pw}')
  
