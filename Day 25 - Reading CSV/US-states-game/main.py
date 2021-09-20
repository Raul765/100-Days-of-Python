import turtle
import pandas

screen  = turtle.Screen()
screen.title("U.S. States Game")
image=r"Day25 - Reading CSV\US-states-game\blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

answers=[]

score=0
data=pandas.read_csv(r"Day25 - Reading CSV\US-states-game\50_states.csv")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")

title="Guess the state"

while score<50:
    
    answer = screen.textinput(title, "What's another state's name")
    answer = answer.title()
    if answer=="Exit":
        missing_states=[]
        for state in data["state"]:
            if state not in answers:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv(r"Day25 - Reading CSV\US-states-game\States_to_learn.csv")
        break

    if answer not in answers:
        for i in range(len(data["state"])):
            if answer==data["state"][i]:
                score+=1
                answers.append(answer)
                writer.setposition(int(data[data["state"]==answer]["x"]),int(data[data["state"]==answer]["y"]))
                writer.write(answer,align="left",font=("Arial", 8, "normal"))

    
    title=f"{score}/50 states correct"