import turtle  #importing turtle for animation
from turtle import * # importing all modules

t=turtle.Turtle()
wn=Screen()

wn.bgcolor("black")#background screen color
t.pensize(40)

t.setposition(0,-270)
t.pendown()
t.begin_fill()
t.color("white")#inner circle
t.pencolor("red")#outer circle
t.circle(270)
t.end_fill()
t.penup()

t.pensize(2)
t.setposition(0,-210)
t.pendown()
t.begin_fill()
t.color("red")#2nd inner circle
t.circle(210)
t.end_fill()
t.penup()

t.pensize(2)
t.setposition(0,-160)
t.pendown()
t.begin_fill()
t.color("#000066")#filling color
t.circle(160)
t.end_fill()
t.penup()

t.pensize(2)
t.setposition(-155,50)
t.pendown()
t.begin_fill()
t.color("white")

for i in range(5):# using for-loop for iterating the work
     t.forward(310)
     t.right(144)
t.end_fill()
t.penup()
turtle.done()

