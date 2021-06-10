import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_list = []

while (len(guessed_list) < 50):
    answer_state = (screen.textinput(title=f"{len(guessed_list)}/50",
                                     prompt="What's another state name?")).title()

    if answer_state == 'Exit':
        learning_list = []
        for i in all_states:
            if i not in guessed_list:
                learning_list.append(i)

        learn_states = {
            "state": learning_list
        }

        ls_to_scv = pandas.DataFrame(learn_states)
        ls_to_scv.to_csv("./states_to_learn.csv")

        break

    if answer_state in all_states and answer_state not in guessed_list:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

