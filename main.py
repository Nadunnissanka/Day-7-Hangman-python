#Step 4

import random
import art
import words

end_of_game = False
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

lives = 6

print(art.logo)
print("\n")
print("Validation is not 100%. This is made to improve my coding knowledge in python.\nThanks for playing!\n")

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print("\nYou guessed this letter already!\n")
      print(f"{' '.join(display)}")
    else:
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter

      #TODO-2: - If guess is not a letter in the chosen_word,
      #Then reduce 'lives' by 1. 
      #If lives goes down to 0 then the game should stop and it should print "You lose."
      if guess not in chosen_word:
          print(f"\nYou guessed a wrong letter! You entered {guess}\n")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")

      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")

      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")

      #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
      print(art.stages[lives])

      