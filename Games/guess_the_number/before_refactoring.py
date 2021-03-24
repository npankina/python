from art import logo
from random import randint

print(logo)

print("Let's play a game. You have to guess a random number from 1 to 100.")
guessed_number = randint(1, 100)
# print(f"Pssst, the guessed number is {guessed_number}.")
level = input("Choose a difficulty level of the game: 'easy' or 'hard?' ")
number_of_attempts = 0
is_continue = True

if level == 'easy':
    number_of_attempts = 10
elif level == 'hard':
    number_of_attempts = 5


def counter_of_attempts():
    global number_of_attempts
    number_of_attempts -= 1
    print(f"You have {number_of_attempts} else.")


while is_continue:
    if number_of_attempts != 0:
        user_input = int(input("\nTry to guess a number! "))
        if user_input == guessed_number:
            print("Congratulations! You win!!")
            is_continue = False
            break
        elif user_input > guessed_number:
            print("Too high.")
            counter_of_attempts()
        elif user_input < guessed_number:
            print("Too small.")
            counter_of_attempts()
    else:
        print("Game over. You lose.")
        is_continue = False
