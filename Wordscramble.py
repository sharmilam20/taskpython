'''2.WORD SCRAMBLE: The player has to unscrumble a jumbled word from the words given in a list format :
word=['python','javascript','java','automation','pytest','guvi','selenium']'''

import random           # statement used for picking random elements from list
word_list = ['python','javascript','java','automation','pytest','guvi','selenium']
original_word = random.choice(word_list)       #Assigning original value is random word from word_list
jumbled_word = "".join(random.sample(original_word,len(original_word)))
'''Here, join is used to merge the characters and return output as a string.The empty string 
stored null value.it Ensure that values are string, as per condition we print "JUMBLED WORD"  '''
 
print("Jumbled Word:",jumbled_word)

while True:        
    user_guess = input("Unscramble Word: ") 
    '''as per condition it take input from user,used lower() for lowercase output then it will
     check the user input is Same or not ,if it  equal it will print"Congrats!,Your guess is correct" '''
    if user_guess.lower() == original_word:
       print("Congrats!,Your Guess is Correct")   
       break              #to end the loop , untill player find correct Word.
    else:
       print("Wrong Answer,Try Again")  
    
    


