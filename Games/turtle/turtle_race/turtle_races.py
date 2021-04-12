from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "green", "yellow", "blue", "purple"]

x_begin = -230
y_begin = -100
shift = 40

all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=x_begin, y=y_begin)
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
    y_begin += shift

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
            break

screen.exitonclick()