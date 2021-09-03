"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
#random number generation
import random
random_number= random.randint(1,99)
your_number=0 
print("Guess a number between 1 and 99")
while your_number != random_number:
    your_number=int(input('Enter Your Number: '))
    if  your_number< random_number:
        print("Sorry your guess is too low  ")
        continue
    elif your_number >random_number:
        print("sorry your guess is too high ")
        continue
    elif your_number==random_number:
        print("Congrats ! the number was ",random_number)
        
       
          
          
