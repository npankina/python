from random import choice
from art import logo
import os


def compare(user, pc):
    if user == pc:
        return "It is a draw 🙃"
    elif pc == 0:
        return "Lose, opponent has blackjack 🙁"
    elif user == 0:
        return "You win with a blackjack 🥳"
    elif user > 21:
        return "You lose 😤"
    elif pc > 21:
        return "Opponent went over. You win 🤩"
    elif user > pc:
        return "You win 🤩"
    else:
        return "You lose 😭"


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    print(logo)
    user_cards = []
    pc_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        pc_cards.append(deal_card())

    while not is_game_over:
        user = calculate_score(user_cards)
        pc = calculate_score(pc_cards)
        print(f"Your cards {user_cards}, current score is {user}")
        print(f"Computer's first card: {pc_cards[0]}")
        if pc == 0 or user == 0 or user > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want one more card? Type 'y' or 'n': ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while pc != 0 and pc < 17:
        pc_cards.append(deal_card())
        pc = calculate_score(pc_cards)

    print(f"Your final hand: {user_cards}, final score: {user}")
    print(f"Computer's final score: {pc_cards}, final scores: {pc}")
    print(compare(user, pc))


play_game()

while input("Do you want to play a game blackjack again? ") == 'y':
    os.system("clear")
    play_game()