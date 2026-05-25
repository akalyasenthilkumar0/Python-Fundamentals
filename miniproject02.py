#---------------------------------------------------------------------------------------------------------
# Miniproject2 : Number Guessing Game
#---------------------------------------------------------------------------------------------------------

print("This is my Miniproject 2")
print("Title : Number Guessing Game")

import random

sec = random.randint(1,10)
print("Secret:", sec) #to know the secrect value assumed randomly

while True: 
  guess=int(input("Enter your guess:"))
  
  if guess == sec:
    print("Congrats!! Your Guess is Correct")
    break
  elif guess > sec:
    print("Your Guess is Too High")
  elif guess < sec:
    print(" Your Guess is Too Low")
  else:
    print("Oops!! It's a Wrong Guessing")
    
print("--------Successfully completed----------")

#------------------------------------------------------------------------------------------------------------
