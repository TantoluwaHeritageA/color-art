# import colorgram
# rgb_colors = []
# colors = colorgram.extract('img.png',20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r,g,b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)
import random
import turtle
# Dimensions of color art
# 10 by 10
# circle radius = 20, gap = 50
import random
# import turtle
import turtle as turtle_module
from turtle import Turtle , Screen
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(233, 224, 210), (217, 159, 89), (42, 109, 148), (123, 164, 190), (216, 232, 222), (149, 64, 87), (202, 135, 156), (35, 130, 95), (178, 159, 37), (124, 179, 153), (235, 216, 223), (159, 81, 53), (210, 89, 64), (209, 223, 232), (194, 87, 112), (227, 199, 118), (60, 164, 133), (139, 32, 43), (10, 103, 78), (51, 157, 179)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20 , random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()