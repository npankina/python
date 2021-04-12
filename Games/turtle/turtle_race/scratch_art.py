from turtle import Turtle, Screen

rik = Turtle()
screen = Screen()


def move_forwards():
    rik.forward(10)


def move_back():
    rik.back(10)


def move_left():
    rik.left(10)


def move_right():
    rik.right(-10)


def clear_drawing():
    rik.clear()
    rik.penup()
    rik.home()
    rik.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
