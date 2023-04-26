import pandas
import turtle

screen = turtle.Screen()
screen.title("US_STATES_GAME")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
with open("50_states.csv") as file:
    state_data = pandas.read_csv(file)
    file.close()

all_states = state_data["state"].to_list()
guessed_states = []
score = 0
is_game_on = True
while is_game_on:
    timmy.penup()
    answer = screen.textinput(f"{score}/50 states guessed", "Guess a state!").title()
    if answer == "Exit":
        to_learn = [state for state in all_states if state not in guessed_states]
        data_table = pandas.DataFrame(to_learn)
        data_table.to_csv("states_to_learn.csv")
        break
    if (state_data["state"] == answer).any():
        guessed_states.append(answer)
        score += 1
        x_coor = int(state_data[state_data["state"] == answer]["x"])
        y_coor = int(state_data[state_data["state"] == answer]["y"])
        timmy.goto(x_coor, y_coor)
        timmy.pendown()
        timmy.write(answer)
    if len(guessed_states) == 50:
        is_game_on = False


