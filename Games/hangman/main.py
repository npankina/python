import random
from hangman_art import logo, stages
from hangman_words import word_list
# from replit import clear

end_of_game = False
lives = 6

print(logo)
chosen_word = random.choice(word_list)
world_length = len(chosen_word)

display = []
for _ in range(world_length):
    display += "_"

guessed_letters = []

while not end_of_game:

    guess = input("Enter a letter: ").lower()
    # clear()

    if guess in guessed_letters:
        print(f"You've already entered this letter. Try again.\n")
    else:
        print(f"You entered letter: {guess}")

    for position in range(world_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(f"{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print("You win!!\n")

    if guess not in display:
        if guess not in guessed_letters:
            print(f"This letter {guess} isn't in the word.\nYou lose a life.")
            lives -= 1
            if lives == 0:
                print("You lose.\n")
                end_of_game = True

    print(stages[lives])
    guessed_letters.append(guess)