#################################
#Author:        Blake Prebeck   #
#Due Date:      7/26/2021       #
#Project:       Turtle Lab #4   #
#################################

#Import Library
import turtle
import time

#Climbing Function
def Climbing(pen_color, pen_size):
    
    #Set Turtle
    TurtleReset()
    turtle.shape('turtle')
    turtle.fillcolor('green')
    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.goto(20, 20)
    turtle.pendown()

    #Climbing Loop
    for i in range(4):
        turtle.forward(50)
        turtle.lt(90)
        turtle.forward(50)
        turtle.rt(90)
    #End Loop

    #Turtle Message
    TurtleMessage('Hurray! Made it to the top!')


#Swimming Function
def Swimming(pen_color, pen_size):
    
    #Set Turtle
    TurtleReset()
    turtle.pensize(pen_size)
    turtle.goto(-200, 100)
    turtle.pendown()

    #Draw Pond
    turtle.pencolor('blue')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(75)
    turtle.end_fill()

    #Draw Path Around Pond
    turtle.shape('turtle')
    turtle.pencolor(pen_color)
    turtle.pensize(pen_size)
    turtle.fillcolor('green')
    turtle.penup()
    turtle.goto(-200, 90)
    turtle.pendown()
    turtle.circle(85)

    #Draw Path Into Pond
    turtle.pencolor('blue')
    turtle.fillcolor('green')
    turtle.lt(90)
    turtle.forward(85)

    #Turtle Message
    TurtleMessage("Yeah! I'm swimming!")


#Eating Function
def Eating():
    
    #Local Variables
    colors = ['red', 'blue', 'yellow', 'cyan']
    count = int(0)

    #Set Turtle
    TurtleReset()

    #Draw Circles Loop
    for i in range(4):
        turtle.penup()
        turtle.goto(-200 + count, -100 + count)
        turtle.pencolor('white')
        turtle.fillcolor(colors[i])
        turtle.pensize(1)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        count = count + 10
    #End loop

    #Reset Count
    count = 0

    #Set Turtle
    turtle.shape('turtle') 

    #Eat Circles Loop
    for i in range(4):
        turtle.penup()
        turtle.goto(-200 + count, -100 + count)
        turtle.pencolor('white')
        turtle.fillcolor('white')
        turtle.pensize(1)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        count = count + 10
        turtle.pencolor('green')
        turtle.fillcolor('green')
        time.sleep(1) 
    #End Loop

    #Turtle Message
    TurtleMessage("Wow!  What a great meal!")


#Sleeping Function
def Sleeping():
        
    #Set Turtle
    TurtleReset()
    turtle.pensize(1)
    turtle.goto(200, -100)
    turtle.pendown()
    turtle.pencolor('chocolate')
    turtle.fillcolor('chocolate')
    turtle.begin_fill()

    #Draw House Loop
    for i in range(4):
        turtle.forward(80)
        turtle.rt(90)
    #End Loop

    #Set Turtle
    turtle.end_fill()
    turtle.penup()
    turtle.goto(225, -115)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.begin_fill()

    #Draw Pillow Loop
    for i in range(4):
        turtle.forward(30)
        turtle.rt(90)
    #End Loop


    #Set Turtle
    turtle.end_fill()
    turtle.penup()
    turtle.lt(90)
    turtle.goto(240, -140)
    turtle.shape('turtle')
    turtle.pencolor('green')
    turtle.fillcolor('green')

    #Turtle Message
    TurtleMessage("Good Night!")


#Turtle Reset Function
def TurtleReset():
    turtle.reset()
    turtle.shape('classic')
    turtle.setup(800, 600)
    turtle.penup()
    turtle.goto(0, 0)


#Turtle Message Function
def TurtleMessage(turtle_message):
    turtle.pencolor('black')
    turtle.write(turtle_message, move=False, align="right", font=("Arial", 12, "bold"))
    time.sleep(3)


#Main Function
def main():
    
    #Climbing Call
    Climbing('grey', 3)

    #Swimming Call
    Swimming('chocolate', 3)

    #Eating Call
    Eating()

    #Sleeping Call
    Sleeping()

#Call main Function
main()
