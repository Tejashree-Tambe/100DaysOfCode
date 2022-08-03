from turtle import Screen
import turtle
from scoreboard import Scoreboard
from write_state import WriteState
import pandas

# scoreboard object
scoreboard = Scoreboard()

# screen
screen = Screen()
screen.title("U.S States Game")

# adding img as background
img_path = "blank_states_img.gif"
screen.addshape(img_path)
turtle.shape(img_path)

# making a list of all guessed states
guessed_states = []

# dialog box asking for state name
data = pandas.read_csv("50_states.csv")

while scoreboard.score < 50:
    state_name = screen.textinput(title=f"{scoreboard.score}/50 states correct", prompt="What's another state name?").title()

    state_data = data[data.state == state_name]

    if state_name == "Exit":
        break

    if not state_data.empty:
        guessed_states.append(state_name)
        state_x_pos = int(state_data.x)
        state_y_pos = int(state_data.y)

        write = WriteState(state=state_name, x_pos=state_x_pos, y_pos=state_y_pos)
        scoreboard.increase_score()

    else:
        print("Doesn't exist")

# making list of states that have not been guessed
all_states = data.state.to_list()

not_guessed_states = []

for state in all_states:
    if state not in guessed_states:
        not_guessed_states.append(state)

    to_learn = pandas.DataFrame(not_guessed_states)
    to_learn.to_csv("states_to_learn.csv")


screen.exitonclick()
