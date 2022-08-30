import colorgram
import turtle as t
import random

tim = t.Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 7 * 12)
screen = t.Screen()
screen.screensize(1000, 1000)
tim.setpos(10, 10)
tim.pensize(20)

#

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202),
              (112, 139, 141), (254, 194, 0)]

print(color_list[0])
print(len(color_list))
print("jestem przed randem")
random.randint(0, len(color_list))
print(color_list[random.randint(0, len(color_list))])
print("jestem tu, przed petla")
for i in range(10):
    tim.setpos(i * 10, 0)
    for j in range(10):
        tim.setpos(i * 10, j * 10)
        color_randomizer = random.choice(color_list)
        print(color_randomizer)
        tim.color(color_randomizer)
        tim.dot

screen.exitonclick
