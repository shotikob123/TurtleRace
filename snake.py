import turtle
from turtle import *
import random
wn = turtle.Screen()
wn.bgcolor('black')

height = 400
width = 400
screen = Screen()
screen.screensize(width, height)



ku1 = turtle.Turtle()
ku1.color('white')
ku2 = turtle.Turtle()
ku2.color('red')
ku3 = turtle.Turtle()
ku3.color('blue')
ku4 = turtle.Turtle()
ku4.color('green')
ku5 = turtle.Turtle()
ku5.color('orange')
ku6 = turtle.Turtle()
ku6.color('purple')
ku7 = turtle.Turtle()
ku7.color('yellow')
ku8 = turtle.Turtle()
ku8.color('pink')
ku9 = turtle.Turtle()
ku9.color('brown')
xazi = turtle.Turtle()
xazi.color('white')
xazi.penup()

xazi.setposition(-400, 240)
xazi.pendown()
xazi.forward(800)
list1 = [ku1, ku2, ku3, ku4, ku5, ku6, ku7, ku8, ku9]
x = -200
y = -200
for i in list1:
    i.penup()
    i.pensize(5)
    i.setposition(x, y)
    x += 45
    i.left(90)
    i.shape('turtle')
    i.pendown()

for b in range(14):
    for j in list1:
        s = random.randint(10, 45)
        j.speed(1)
        j.forward(s)

turtle.done()
