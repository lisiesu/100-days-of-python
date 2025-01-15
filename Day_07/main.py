# HANGMAN GAME => To practice loops

import random
import hangman_words
import hangman_art

lives = 6
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess in correct_letters:
                print(f"You have already guessed {guess}")
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        print(f"You chose {guess}. Unfortunately that is WRONG. You lose a life!")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(hangman_art.stages[lives])