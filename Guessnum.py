# 1.Guess the Number:
#Cooncept: The computer randomly Selects a number within in a range ,and the player has to guess it

import random
#giving some random range
num_to_guess = random.randint(7,15)
#Here, we use while loop so multiple guesses are allowed(inputs allowed untill we guess write number)
while True :
    user_guess = int(input()) #Assigned User guess as a user input

    if user_guess < num_to_guess: 
        print("Too Low,Try Again")

        '''Here using "if condition" for user input is lesser then computer selected number "
    "we show notificatin "Too low,try again"  print("Too low,Try Again"
    * if it show too low then we try greater number to find computer guess)'''
  
    elif user_guess > num_to_guess:
      print("Too High,Try Again")

      '''user input is greater then Computer selected number then it print "Too high,try again",
        with this we try lowest number to get correct guess'''
    
    else:  # If the input is equal to the computer guess it prints Congrats!,You Guess it"
        print("Congrats!, You Guess it")
        break # using Break statement for end this loop 