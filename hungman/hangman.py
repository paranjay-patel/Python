import random
from words import words
word_list = words

chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
lives = 6
stages = ['''

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
========

''',
'''

  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
========

''','''

  +---+
  |   |
  0   |
 /|\  |
      |
      |
========

''','''
  +---+
  |   |
  0   |
 /|   |
      |
      |
========

''','''
  +---+
  |   |
  0   |
 /    |
      |
      |
========

''','''
  +---+
  |   |
  0   |
      |
      |
      |
========

''','''
  +---+
  |   |
      |
      |
      |
      |
========

''']

for i in range(len(chosen_word)):
    display.append("_")

print("\n***********************************")
print("             HANGMAN    ")
print("***********************************\n")

print(display)
end_of_game = False
while not end_of_game:
    guess = input("guess a letter : ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess       
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("******you lose.")
        
    if "_" not in display:
        end_of_game = True
        print("******you win.")

    print(display)
    print(stages[lives]) 
