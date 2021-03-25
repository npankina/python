from art import logo, vs
from game_data import data
from random import choice
import os


def clear():
    os.system('clear')

def get_random_account():
    choice_item = choice(data)
    return choice_item

def format_data(choice_item):
    """Takes the accountant data and returns the printable format."""
    name = choice_item['name']
    description = choice_item['description']
    country = choice_item['country']
    return f"{name}, {description}, {country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    scores = 0
    is_game_contunue = True
    account_b = get_random_account()

    while is_game_contunue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers_count = account_a["follower_count"]
        b_followers_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_followers_count, b_followers_count)

        if is_correct:
            scores += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {scores}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {scores}")
            is_game_contunue = False


game()
