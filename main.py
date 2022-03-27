import random
from turtle import Turtle, Screen
# import colorgram


rgb_colors = [(157, 81, 35), (57, 30, 17), (221, 153, 66), (53, 19, 30), (20, 29, 47), (194, 143, 35), (134, 34, 19),
              (236, 212, 81), (52, 95, 133), (23, 36, 28), (242, 232, 191), (68, 112, 84), (129, 68, 89), (221, 92, 47),
              (88, 74, 22), (118, 31, 45), (127, 180, 143), (210, 240, 220), (114, 167, 199), (43, 52, 107),
              (207, 230, 243), (84, 157, 110), (152, 219, 163), (188, 138, 158), (35, 83, 61), (181, 90, 116),
              (107, 111, 176), (54, 157, 181), (22, 81, 96), (238, 215, 226)]

# Code used to generate rgb color listed above
# colors = colorgram.extract('COLORFUL-NIGHT.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

# 10 x 10 grid of dots about 20 big 50 apart
screen = Screen()
screen.colormode(255)

turt = Turtle()
turt.pensize(20)
turt.hideturtle()
turt.speed("fastest")
turt.penup()

for y in range(10):
    for x in range(10):
        turt.setposition((1 + (x * 50)), (1 + (y * 50)))
        turt.dot(20, random.choice(rgb_colors))

screen.exitonclick()
