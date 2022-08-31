import colorgram
import turtle as t
import random

tim = t.Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 7 * 12)
screen = t.Screen()
screen.screensize(canvwidth=250/2, canvheight=250/2)
screen.colormode(255)
tim.setpos(0, 0)
tim.pensize(10)
tim.penup()
tim.speed(100)


# for color in colors:
#     rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243),
              (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208),
              (168, 99, 102), (66, 64, 60), (219, 178, 183),
              (178, 198, 202), (112, 139, 141), (254, 194, 0)]

for i in range(-5, 5):
    print(tim.position())
    tim.penup()
    tim.setpos(i * 50, 0)
    for j in range(-5, 5):
        print(tim.position())
        tim.setpos(i * 50, j * 50)
        color_randomizer = random.choice(color_list)
        print(color_randomizer)
        tim.color(color_randomizer)
        tim.pendown()
        tim.dot()
        tim.penup()
    tim.penup()

screen.exitonclick
