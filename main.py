import pandas
import turtle

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
text_generator = turtle.Turtle(visible=False)
text_generator.penup()
screen = turtle.Screen()
screen.setup(725, 491)
screen.bgpic('blank_states_img.gif')

states_guessed = []
while len(states_guessed) < 50:
    user_input = screen.textinput(f"{len(states_guessed)}/50 Correct", "Guess a state: ").title()
    while user_input in states_guessed:
        user_input = screen.textinput(f"{len(states_guessed)}/50 Correct", f"You already guessed {user_input}: ").title()
    if user_input in states:
        state_data = data[data.state == user_input]
        text_generator.goto(int(state_data.x), int(state_data.y))
        text_generator.write(user_input, align='center')
        states_guessed.append(user_input)
    elif user_input == "Exit":
        missed_states = [state for state in states if state not in states_guessed]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

text_generator.goto(0,0)
text_generator.write(f"You listed {len(states_guessed)}/50 states correctly", align='center', font=['Courier', 20, 'normal'])


screen.exitonclick()
