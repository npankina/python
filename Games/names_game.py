import random

list_woman = ['Amanda', 'Jane', 'Sarah', 'Olivia']
list_man = ['Jason', 'Ed', 'Owen', 'James']
gender = ''

def random_man_name():
    i = random.randint(0, 3)
    print(f"Hello, {list_man[i]}. Nice to meet you!")


def random_name_woman():
    i = random.randint(0, 3)
    print(f"Hello, {list_woman[i]}. Nice to meet you!")


name = input(
    "Hello. What is your name? If you don't want to tell your real name - tap 0 - and we will chose one random name for you. ")

if name == '0':
    gender = input("What is your gender? M or W: ")
    gender.lower()
if name == '0' and gender == 'm':
    random_man_name()
elif name == '0' and gender == 'w':
    random_name_woman()
if name != '0':
    print(f"Hello, {name}. Nice to meet you.")
