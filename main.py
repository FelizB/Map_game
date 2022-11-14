import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    Answer = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                              prompt="What another state's do you know?").title()
    if Answer == "Exit":
        missing_states= []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        st= pandas.DataFrame(missing_states)
        st.to_csv("output")
        print(f"Thank you for your time. You scored {len(guessed_states)}/50.\nHere is the list of the missed states"
              f"\n{st}")
        break
    if Answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == Answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

        if Answer not in guessed_states:
            guessed_states.append(Answer)




turtle.exitonclick()

