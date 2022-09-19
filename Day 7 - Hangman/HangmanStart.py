# for char in selected_word_list:
#     # Adds "_" to display for each character in list
#     display += "_"
#     # if guess = character, print "Right"
#     if guess == char:
#         print("Right")
#         # Iterate over list items by index pos
#         for i in range(0, len(selected_word_list)):
#             # Check if items matches the given element
#             if selected_word_list[i] == guess:
#                 guess_location += [i]
#                 guess_location = list(dict.fromkeys(guess_location))
#                 for n in range(0, len(guess_location) - 1):
#                     display[guess_location[n]] = guess[n]
#             else:
#                 print("Wrong")
            
        
# print(display)
# print(guess_location)



#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
import random
from re import A
from unittest import result

# end_range = len(word_list) - 1

word_list = ["aardvark", "baboon", "camel", "appalachia"]
correct_answer = random.choice(word_list)
word_length = len(correct_answer)
display = []
for _ in range(word_length):
    # Adds "_" to display for each character in list
    display += "_"
    # if guess = character, print "Right"
print(display)
# print(correct_answer)
game_over = False
display_update = []

def check_guess():
    guess = input("Guess a letter. ").lower()
    for l in range(word_length):
        if correct_answer[l] == guess:
            display[l] = guess
        if correct_answer[l] != "_":    
            pass    
        else:
            display[l] = "_"
    print(display) 
    display_update = display
    guess = input("Guess a letter. ").lower()
    for l in range(word_length):
        if correct_answer[l] == guess:
            display_update[l] = guess
        if correct_answer[l] != "_":    
            pass
        else:
            display_update[l] = "_"
    print(display_update) 
    return display_update   


while game_over == False:
    check_guess()
































# Working code for replacing blanks with letters and updating display
# def check_guess():
#     guess = input("Guess a letter. ").lower()
#     for l in range(word_length):
#         if correct_answer[l] == guess:
#             display[l] = guess
#         else:
#             display[l] = "_"
#     print(display) 
#     return display   


# display_update = check_guess()

# def check_again():
#     guess = input("Guess a letter. ").lower()
#     for l in range(word_length):
#         if correct_answer[l] == guess:
#             display_update[l] = guess
#         if correct_answer[l] != "_":    
#             pass
#         else:
#             display_update[l] = "_"
#     print(display_update) 
#     return display_update   

# check_again()
