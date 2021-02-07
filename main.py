import turtle as t
import random
from color import color_list


dolmus = t.Turtle()
dolmus.shape("arrow")
dolmus.speed(5)
dolmus.pensize(20)
dolmus.penup()

t.colormode(255)

for y in range(-225, 226, 50):
    for x in range(-225, 226, 50):
        dolmus.goto(x, y)
        dolmus.dot(20, random.choice(color_list))


screen = t.Screen()
screen.exitonclick()
