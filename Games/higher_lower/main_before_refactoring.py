from art import logo, vs
from game_data import data
from random import choice
import os


def clear():
    os.system('clear')


def random_person():
    choice_item = choice(data)
    return choice_item


def render_person(choice_item):
    name = choice_item['name']
    follower_count = choice_item['follower_count']
    description = choice_item['description']
    country = choice_item['country']
    return name, follower_count, description, country


def game():
    scores = 0
    print(logo)

    flag = True
    person_b = render_person(random_person())

    while flag:
        person_a = person_b
        person_b = render_person(random_person())

        print(f"Compare A: {person_a[0]}, {person_a[2]}, {person_a[3]}")
        print(vs)
        print(f"Against B: {person_b[0]}, {person_b[2]}, {person_b[3]}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess == 'a':
            guess_new = person_a[1]
            answer = person_b[1]
        else:
            guess_new = person_b[1]
            answer = person_a[1]

        if guess_new > answer:
            scores += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {scores}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {scores}")
            flag = False


game()
