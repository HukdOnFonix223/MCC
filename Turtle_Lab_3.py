#Author:        Blake Prebeck
#Due Date:      7/14/2021
#Project:       Turtle Lab #3

#Description:   Final program draws circles of random size, pen size, fill color and location.

#Import Library
import turtle
import time
import random

#Variables
horizontal = int()
radius = int()
colors = ["red", "blue", "yellow", "green"]
pen_size = int()
t = turtle.Turtle()
random_index = int()

#Initializing location and size of circles
horizontal = -200
radius = 25
pen_size = 2

#Turtle starting point
t.penup()
t.goto(-200,0)
t.pendown()

#Initialize the pensize by typing in
t.pensize(5)

#Loop to draw the circles
for count in range(0, 4):
    t.fillcolor(colors[count])
    t.pensize(pen_size)
    t.begin_fill()
    
    #Draw circle
    t.circle(radius)

    #Reset location, radius and pen size
    horizontal = horizontal + 75
    radius= radius + 20
    pen_size = pen_size + 2
    #Moving the turtle
    t.penup()
    t.goto(horizontal, 0)
    t.pendown()
    t.end_fill()
    #End loop

#Reset
time.sleep(3)
t.reset()
turtle.setup(600, 600)

#Write message
t.penup()
t.goto(0, 0)
t.pendown()
t.write("Ready for more circles?", move=False, align="center", font=("Arial",16, "bold"))

#Reset
time.sleep(3)
t.reset()
turtle.setup(600, 600)

#Create circles loop
for count2 in range(1,21):
    random_index = random.randint(0,3)
    t.penup()
    t.goto(random.randint(-150, 150), random.randint(-150, 150))
    t.fillcolor(colors[random_index])
    t.pensize(random.randint(0, 10))
    t.pendown()
    t.begin_fill()
    t.circle(random.randint(25, 125))
    t.end_fill()
    #End loop
