import random

word_list = ["aardvark", "baboon", "camel", "milk", "book"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_int_gen = random.randint(0,len(word_list)-1)
chosen_word = word_list[random_int_gen]


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please enter your guessed letter: ").lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
letter_list = list(chosen_word)

for letter in letter_list:
  if letter == guess:
    print(f"Right - {letter}")
  else:
    print(f"Wrong - {letter}")
