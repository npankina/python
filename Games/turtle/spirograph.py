import turtle as t
from random import randint

ken = t.Turtle()
t.colormode(255)

ken.speed("fastest")


def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        ken.color(random_colors())
        ken.circle(100)
        ken.setheading(ken.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
