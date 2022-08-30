import turtle
import pandas   

screen = turtle.Screen()
screen.title("U.S. states game")
image = "us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("us_states_game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []
ungessed_states = []

while len(guessed_states) < 50:
    answer_state =  screen.textinput(title=f"{len(guessed_states)}/50 state currect",prompt="what's another state's name?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                ungessed_states.append(state)
        print(ungessed_states)
        new_data = pandas.DataFrame(ungessed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(answer_state)


# print(pandas.DataFrame({"unguessed_states":ungessed_states}))















screen.exitonclick()