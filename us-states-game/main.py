import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_name = turtle.Turtle()


data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the States", prompt="Enter a state name").title()
score = 0
correct_answers = []
while True:
    states = data.state
    if answer_state == "Exit":
        break
    elif states.str.contains(answer_state).any():
        if answer_state in correct_answers:
            answer_state = screen.textinput(title=f"{score}/50 States correct",
                                            prompt="You already answered that. Pick another state").title()

        else:
            score = score + 1
            correct_answers.append(answer_state)
            answer = data[data.state == answer_state]
            x_pos = int(answer.x.to_string(index=False))
            y_pos = int(answer.y.to_string(index=False))
            state_name.penup()
            state_name.hideturtle()
            state_name.goto(x_pos, y_pos)
            state_name.write(answer_state, False, align="center", font=("Arial", 10, "bold"))
            answer_state = screen.textinput(title=f"{score}/50 States correct",
                                            prompt="What's another state's name").title()
    else:
        answer_state = screen.textinput(title=f"{score}/50 States correct",
                                        prompt="Invalid answer. Try again").title()




# write to csv states that were not guessed
all_states = data.state.to_list()
missing_states = []
for state in all_states:
    if state not in correct_answers:
        missing_states.append(state)


missing_states = pandas.DataFrame(missing_states)

missing_states.to_csv("states_to_learn.csv")







# print(data[data.state == answer_state])


# # get x coor
# answer = data[data.state == answer_state]
# print(answer.x.to_string(index=False))

# monday = data[data.day == "Monday"]
# temp_in_c = monday.temp
# temp_in_f = (temp_in_c * (9/5)) + 32
# print(temp_in_f)






screen.exitonclick()