from turtle import Turtle, Screen

olovka = Turtle()
ekran = Screen()

def move_forawrds():
    olovka.forward(10)

def move_backwards():
    olovka.backward(10)

def rotate_clockwise():
    novi_heading = olovka.heading() + 10
    olovka.setheading(novi_heading)

def rotate_counter_clockwise():
    novi_heading = olovka.heading() - 10
    olovka.setheading(novi_heading)
def clear():
    olovka.clear()
    olovka.penup()
    olovka.home()
    olovka.pendown()

ekran.listen()
ekran.onkey(key="w",fun=move_forawrds)
ekran.onkey(key="s",fun=move_backwards)
ekran.onkey(key="a",fun=rotate_clockwise)
ekran.onkey(key="d",fun=rotate_counter_clockwise)
ekran.onkey(key="c",fun=clear)

ekran.exitonclick()
#
# ekran.listen()
# ekran.onkey(key="space", fun=move_forawrds)
# ekran.exitonclick()