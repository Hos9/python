import string
import random
 
def generate_password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for char in range(size):
        rand_char = random.choice(all_chars)
        password = password + rand_char
    return password
 
pass_len = int(input('How many characters in your password?'))
new_password = generate_password(pass_len)
print('Your new password: ', new_password)

print('''
______________________________________
''')

import string
import random

def g_p(a):
  chars = string.ascii_letters + string.digits + string.punctuation
  pw = ''
  for i in range(a):
    r_c = random.choice(chars)
    pw = pw + r_c
  return pw
  
p_l = int(input('pw length? '))
n_pw = g_p(p_l)
print('pw is: ', n_pw)

