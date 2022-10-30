# import random
# import random as r

# print(random.randint(0, 100))
# print(r.randint(0, 100))

# from random import  randint
# print(randint(0, 100))

# import random as r
# lst = [0, 1, 2, 3, 4, 5]
# r.shuffle(lst)
# print(lst)

import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.width(6)
t.color("red")

horizontal = 200
vertical = 100

t.fd(horizontal)
t.right(90)
t.fd(vertical)
t.right(90)
t.fd(horizontal)
t.right(90)
t.fd(vertical)
t.right(90)

t.penup()
t.goto(120, -30)
t.pendown()
t.fd(50)
t.circle(30)
t.write("movavi", font=("arial black, 50, "normal"))

screen.exitonclick()