import turtle as t
from random import choice

color_list = [(245, 245, 238), (238, 247, 239), (203, 170, 118), (153, 144, 49), (140, 120, 25), (121, 32, 11), (94, 68, 77), (221, 144, 149), (67, 131, 128), (91, 38, 29), (240, 244, 249), (248, 238, 242), (206, 89, 92), (218, 204, 30), (4, 89, 84)]

ken = t.Turtle()
ken.hideturtle()
t.colormode(255)
ken.speed("fastest")


ken.penup()
ken.setheading(225)
ken.forward(300)
ken.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    ken.dot(20, choice(color_list))
    ken.forward(50)

    if dot_count % 10 == 0:
        ken.setheading(90)
        ken.forward(50)
        ken.setheading(180)
        ken.forward(500)
        ken.setheading(0)




screen = t.Screen()
screen.exitonclick()
