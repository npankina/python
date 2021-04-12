from turtle import Turtle, Screen
from random import choice

ken = Turtle()

ken.shape("turtle")
ken.color("steel blue")

colors = [
    "CadetBlue",
    "chartreuse3",
    "cyan4",
    "DarkBlue",
    "DarkOrange1",
    "bisque3",
    "coral1",
    "brown4",
    "DarkOrchid1"
]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        ken.forward(100)
        ken.right(angle)

for shape_sides in range(3, 11):
    ken.color(choice(colors))
    draw_shape(shape_sides)


screen = Screen()
screen.exitonclick()