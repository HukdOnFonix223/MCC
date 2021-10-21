############################################################
# Authors:          Blake Prebeck   
#                   Randolph Chabot         
#                   Alexander Berlingieri   
#      
# Assignment:       Turtle Lab 5      
#      
# Date:             08/11/2021            
#  
# Description:      Turtle Car Dealership
#                   User selects model and color of car.
#                   Program outputs price, model, color and draws car.
#
############################################################

# At least 4 functions.  One of these functions will be main().
    #Function 1: CarList()
        #List of model and prices
        #Outputs list with single loop
        #User inputs model choice
        #Return model and price

    #Function 2: CarColor()
        #List of colors and prices
        #Outputs list with single loop
        #User inputs car make/model and color
        #If structure for car pricing by color
        #Return color and price

    #Function 3: CarOutput()
        #Data In: model, model price, color, and color price
        #Calculate total price
        #Output color, model and total price

    #Function 4: TurtleCarArt()
        #Data In: color
        #Creates turtle art of car in selected color
        #Creates tires with nested loop

    #Function 5: TurtleAsk()
        #Data In: color
        #Asks user if they want to see their car drawn in turtle
    
    #Function 6: main()
        #Calls all other functions

############################################################

# At least one function needs to demonstrate the proper usage of a list.
     #Completed

# At least one function needs to demonstrate a single loop.
    #Completed

# At least one function needs to demonstrate a nested loop.
    #Completed

# At least one function needs to demonstrate the use of a multi-alternative IF structure.
    #Completed

# One function needs to contain an input statement.
    #Completed

# One function needs to output something to the screen.
    #Completed

############################################################

#Select Car Model Function
def CarList():

    #Index List
    list_index = ['[1]', '[2]', '[3]', '[4]', '[5]']
    #Model List
    list_cars = ['Focus Ti', 'Taurus SE', 'F-150 XL', 'Mustang', 'GT Super']
    #Pricing List
    list_prices = [17950, 31200, 29290, 27205, 500000]
    
    #Selection Menu
    print('*******************************')
    print('******** Cars For Sale ********')
    print('*******************************')
    print('Model\t\t\tPrice')

    #Print Car and Pricing List (Single Loop)
    for i in range(len(list_cars)):
        print(list_index[i], list_cars[i], '\t\t$', list_prices[i])
    
    #User input
    user_ans = int(input("\nSelect the model number you're interested in:  "))
    
    #Return Model and Price
    return [list_cars[user_ans-1], list_prices[user_ans-1]]


#Select Car Color Function
def CarColor():

    #Local Variables
    color = str()
    price = float()

    #Color List
    list_colors = ['[1] Blue', '[2] Purple', '[3] Black', '[4] Green', '[5] Yellow', '[6] Red', '[7] Gold']
    
    #Color Prices List
    list_colors_price = [0, 0, 0, 0, 250, 500, 1000]
    
    #Selection Menu
    print('*******************************')
    print('******* Color Selection *******')
    print('*******************************')
    print('Color\t\t\tPrice')
    
    #Print Colors and Pricing List (Single Loop)
    for i in range(len(list_colors)):
        print(list_colors[i], '\t\t$', list_colors_price[i])

    #User input
    user_ans = int(input("\nEnter the number of the color you would like:  "))
    
    #Color Pricing
    if user_ans == 1:
        color = 'Blue'
        price = 0
    elif user_ans == 2:
        color = 'Purple'
        price = 0
    elif user_ans == 3:
        color = 'Black'
        price = 0
    elif user_ans == 4:
        color = 'Green'
        price = 0
    elif user_ans == 5:
        color = 'Yellow'
        price = 250
    elif user_ans == 6:
        color = 'Red'
        price = 500
    elif user_ans == 7:
        color = 'Gold'
        price = 1000

    #Return Color and Price
    return [color, price]


#Car Output Function
def CarOutput(in_model, in_model_price, in_color, in_color_price):
    
    #Total Car Pricing
    car_total = in_model_price + in_color_price

    #Print Outputs
    print('\nCongratulations on your new', in_color, 'Ford', in_model, '!')
    print('\nYour total vehicle cost is: $', car_total)


#Draw Car Turtle Art Function
def TurtleCarArt(color):
    
    #Import Library 
    import turtle
    import time

    #Local Variables
    sedan = turtle.Turtle()
    
    #Below code for drawing rectangular upper body
    sedan.color(color)
    sedan.fillcolor(color)
    sedan.penup()
    sedan.goto(-100,0)
    sedan.pendown()
    sedan.begin_fill()
    sedan.forward(370)
    sedan.left(90)
    sedan.forward(50)
    sedan.left(90)
    sedan.forward(370)
    sedan.left(90)
    sedan.forward(50)
    sedan.left(90)
    sedan.end_fill()
    sedan.penup()
    sedan.left(90)
    sedan.forward(50)
    sedan.right(90)
    sedan.pendown()
    sedan.pencolor('black')
    sedan.fillcolor('gray')
    sedan.begin_fill()
    sedan.forward(40)
    sedan.right(90)
    sedan.forward(25)
    sedan.right(90)
    sedan.forward(40)
    sedan.right(90)
    sedan.forward(25)
    sedan.right(90)
    sedan.forward(40)
    sedan.end_fill()
    sedan.penup()
    sedan.forward(60)
    sedan.pendown()
    #Makes sure no black on black
    if color != 'Black':
        sedan.pencolor('black')
    else:
        sedan.pencolor('white smoke')
    sedan.right(90)
    sedan.forward(50)
    sedan.left(90)
    sedan.forward(99)
    sedan.left(90)
    sedan.forward(50)
    sedan.left(90)
    sedan.forward(99)
    sedan.penup()
    sedan.right(180)
    sedan.forward(70)
    sedan.right(90)
    sedan.forward(15)
    sedan.pendown()
    sedan.pensize(4)
    #Makes sure no black on black
    if color != 'Black':
        sedan.pencolor('black')
    else:
        sedan.pencolor('white smoke')
    sedan.right(90)
    sedan.forward(20)
    
    # Below code for drawing window and roof
    sedan.pencolor(color)
    sedan.penup()
    sedan.goto(0, 50)
    sedan.pendown()
    sedan.setheading(45)
    sedan.forward(70)
    sedan.setheading(0)
    sedan.forward(100)
    sedan.setheading(-45)
    sedan.forward(70)
    sedan.setheading(90)
    sedan.penup()
    sedan.goto(100, 50)
    sedan.pendown()
    sedan.forward(49.50)

    # Below code for drawing two tires (Nested Loop)
    loop1 = 0
    sedan.penup()
    sedan.goto(0, -10)
    sedan.color('#000000')
    sedan.fillcolor('silver')
    while loop1 != 2:
        for i in range(1):
            sedan.pendown()
            sedan.begin_fill()
            sedan.circle(20)
            sedan.end_fill()
            sedan.penup()
            sedan.goto(200, -10)
            loop1 += 1
    
    #Keeps Window Open
    sedan.hideturtle()
    sedan.penup()
    sedan.goto(-100, -100)
    sedan.pendown()
    sedan.write("That looks like a sweet ride!", move=False, align='left', font=('Times New Roman', 14, 'normal')) 
    time.sleep(3)


#Car Turtle Art Output
def TurtleAsk(in_color):
    #User input
    user_ans = input('\nWould you like to see your car?  Enter "Y" or "N":  ')
    
    if user_ans == 'Y':
        print('\nEnjoy your new vehicle!  Goodbye!')
        #Calls turtle art drawing function
        TurtleCarArt(in_color)
    else:
        print('\nEnjoy your new vehicle!  Goodbye!')


#Define main()
def main():

    #Run CarList() Function
    result1 = CarList()

    #Run CarColor() Function
    result2 = CarColor()
    
    #Run CarOutput() Function
    CarOutput(result1[0], result1[1], result2[0], result2[1])
    
    #Run TurtleAsk() Function
    TurtleAsk(result2[0])


#Run main() Function
main()
