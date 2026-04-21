import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
# turtle_module.colormode(255) - colormode pravi problem
colors = colorgram.extract("slika1.jpg", 100)

olovka = turtle_module.Turtle()
# ekran = turtle_module.Screen()
olovka.penup()
olovka.speed("fast")
olovka.setheading(0)
olovka.setheading(225)
olovka.forward(300)
olovka.setheading(0)
olovka.hideturtle()
# ekran.exitonclick()
num_of_dots = 100

# boje = []
boje = [(246, 244, 243), (235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209), (65, 66, 56), (103, 140, 129), (164, 200, 214), (130, 129, 122)]



# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     nova = (r,g,b)
#     boje.append(nova)

# print(boje)
# olovka.dot(20,(248, 245, 237))

for broj in range(1, num_of_dots + 1):
    olovka.dot(20,random.choice(boje))
    olovka.forward(50)

    if broj % 10 == 0:
        olovka.setheading(90)
        olovka.forward(50)
        olovka.setheading(180)
        olovka.forward(500)
        olovka.setheading(0)












#KOD ZA EXTRACT BOJA IZ SLIKE PREKO COLORGRAM.PY
# rgb_colors = []
# hsl_colors = []
# colors = colorgram.extract("slika.jpg", 10)

# for color in colors:
#     rgb_colors.append(color.rgb)
#     hsl_colors.append(color.hsl)
#
# print(rgb_colors)
# print(hsl_colors)

# color_tuples = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_tuples.append(new_color)
#
# print(color_tuples)