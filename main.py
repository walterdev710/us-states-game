import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
# print(states)

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

counting = 0



while len(guessed_states) < 50:
    
    usr_answer = screen.textinput(title=f"{counting}/50 States Correct", prompt="What's another state's name?").title()
    
    if usr_answer == "Exit":
        missed_states = []
        for missing_state in all_states:
            if missing_state not in guessed_states:
                missed_states.append(missing_state)
                
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")    
        break
    
    if usr_answer in all_states:
        counting +=1
        guessed_states.append(usr_answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        position = data[data["state"] == usr_answer]
        t.goto(int(position.x), int(position.y))
        t.write(position.state.item())

# states_to_learn.csv

        
