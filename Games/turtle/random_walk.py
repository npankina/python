import turtle as t
from random import choice, randint

ken = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]
ken.pensize(15)
ken.speed("fastest")

def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

for _ in range(200):
    ken.color(random_colors())
    ken.forward(30)
    ken.setheading(choice(directions))

screen = t.Screen()
screen.exitonclick()