#Author:        Blake Prebeck
#Date:          7/5/2021
#Assignment:    Turtle Lab 2

#Import Library
import turtle
import time

#Variables
t = turtle.Turtle()
pen_color =str()
fill_color = str()
pen_size =int()

#Moving the pen
t.penup()
t.goto(0, 150)
t.pendown()


#Input
pen_color = input("Pen Color, choose red, blue or yellow:  ")
pen_size = int(input("Pen Size, select 1 to 10:  "))

#Decision Structure
if pen_color == "red":
    fill_color = "yellow"
elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color = "green"

#Turtle Parameters
t.pensize(pen_size)
t.pencolor(pen_color)
t.fillcolor(fill_color)

#Start Fill
t.begin_fill()

#Draw Circle
t.circle(50)

#Stop Fill
t.end_fill()

#Moving the pen
t.penup()
t.rt(90)
t.forward(50)
t.pendown()

#Input
pen_color = input("Pen Color, choose red, blue or yellow:  ")

#Turtle Pen Color
t.pencolor(pen_color)

#Decision Structure
if pen_color == "red":
    fill_color = "yellow"
elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color = "green"

#Fill Color
t.fillcolor(fill_color)

#Start Fill
t.begin_fill()

#Drawing a Square
t.rt(90)
t.forward(50)
t.lt(90)
t.forward(100)
t.lt(90)
t.forward(100)
t.lt(90)
t.forward(100)
t.lt(90)
t.forward(50)

#Stop Fill
t.end_fill()

#Moving the pen
t.penup()
t.lt(90)
t.forward(150)
t.pendown()

#Input
pen_color = input("Pen Color, choose red, blue or yellow:  ")

#Turtle Pen Color
t.pencolor(pen_color)

#Decision Structure
if pen_color == "red":
    fill_color = "yellow"
elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color = "green"

#Fill Color
t.fillcolor(fill_color)

#Start Fill
t.begin_fill()

#Drawing the Triangle
t.rt(35)
t.forward(125)
t.rt(235)
t.forward(150)
t.lt(127)
t.forward(130)

#Stop Fill
t.end_fill()


#On Your Own
time.sleep(3)
t.reset()
turtle.setup(600, 600) #sets up the size of the window

#Input
SHAPE = input("Choose square or circle:  ")
LOCATION = input("Choose Location, Top Left, Top Right, Bottom Left and Bottom Right:  ")

#Shape Selection
if SHAPE == "square":
    fill_color = input("Fill Color, choose red, blue or yellow:  ")
   
    #Decision Structure
    if fill_color == "red":
     pen_color = "yellow"
    elif fill_color == "blue":
        pen_color = "red"
    else:
        pen_color = "green"

else:
    pen_color = input("Pen Color, choose red, blue or yellow:  ")

    #Decision Structure
    if pen_color == "red":
     fill_color = "yellow"
    elif pen_color == "blue":
        fill_color = "pink"
    else:
        fill_color = "green"

#Turtle Parameters
t.pensize(pen_size)
t.pencolor(pen_color)
t.fillcolor(fill_color)

#Shape Location
if LOCATION == 'Top Left':
    #Moving the pen
    t.penup()
    t.goto(-200, 200)    
    t.pendown()

    #Set Size
    t.pensize(3)

elif LOCATION == 'Top Right':
    #Moving the pen
    t.penup()
    t.goto(200, 200)    
    t.pendown()

    #Set Size
    t.pensize(5)

elif LOCATION == 'Bottom Left':
        #Moving the pen
    t.penup()
    t.goto(-200, -200)    
    t.pendown()

    #Set Size
    t.pensize(7)

else:
    #Moving the pen
    t.penup()
    t.goto(200, -200)    
    t.pendown()

    #Set Size
    t.pensize(9)

#Draw Shapes
if SHAPE == 'square':

    #Start Fill
    t.begin_fill()

    #Drawing a Square
    t.forward(50)
    t.lt(90)
    t.forward(100)
    t.lt(90)
    t.forward(100)
    t.lt(90)
    t.forward(100)
    t.lt(90)
    t.forward(50)

    #Stop Fill
    t.end_fill()
else:
    #Start Fill
    t.begin_fill()

    #Draw Circle
    t.circle(50)

    #Stop Fill
    t.end_fill()
    
