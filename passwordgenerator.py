# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:03:29 2023

@author: Harshini Vanga
"""

import string
import random
 
length = int(input("Enter the password length: "))
 
print('''Choose character set for password  :
         1. Digits
         2. Letters
         3. Special characters
         4. Leave''')
 
characterList = ""
 
# Getting character set for password
while(True):
    select = int(input("choose a number "))
    if(select == 1):
        characterList += string.ascii_letters
    elif(select == 2):
        characterList += string.digits
    elif(select== 3):
        characterList += string.punctuation
    elif(select == 4):
        break
    else:
        print("Do pick a valid choice as input")
 
password = []
 
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
 #password to be printed is
print("The random password is " + "".join(password))