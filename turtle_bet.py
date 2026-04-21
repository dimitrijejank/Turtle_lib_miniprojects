from turtle import Turtle, Screen
import random

olovka = Turtle()
olovka.penup()
olovka.goto(x=230,y = 130)
olovka.pensize(3)
olovka.pendown()
olovka.goto(x=230,y = -130)
olovka.penup()
ekran = Screen()
ekran.setup(height=400,width=550)
izbor_boja = ekran.textinput(title="Make a bet!", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
sve_kornjace = []

for turtle_index in range (0,6):
    kor1 = Turtle(shape="turtle")
    kor1.color(colors[turtle_index])
    kor1.penup()
    kor1.goto(x=-200, y=y_positions[turtle_index])
    sve_kornjace.append(kor1)

if izbor_boja:
    is_race_on = True

while is_race_on:
    for turtle in sve_kornjace:
        if turtle.xcor() > 230:
            is_race_on = False
            if izbor_boja == turtle.pencolor():
                ekran.title("YOU WON")
                print("YOU WON!!!")
            else:
                ekran.title("YOU LOST")
                print(f"You lost, the winner is {turtle.pencolor} turtle!")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)



print(izbor_boja)
ekran.exitonclick()