import turtle

""""
This python program will display 3 different shapes(circle,square,hexagon),and ask the user to put in the color
of each shape. Turtle method will be used to draw these shapes.
"""

def setPostion(turta, x, y): #here we set the postion of each shape
    turta.penup()
    turta.goto(x, y)
    turta.pendown()

def circle(turta,circle_color,border_color): #here is where turtle draws the circle shape
    turta.fillcolor(circle_color)
    turta.pencolor(border_color)

    setPostion(turta,0,0) # postion of the 1st circle
    turta.begin_fill()
    turta.circle(30) # diameter
    turta.end_fill()
    
    setPostion(turta,-70,70) # postion of the 2nd circle
    turta.begin_fill()
    turta.circle(30)
    turta.end_fill()
    
    setPostion(turta,70,-70) # postion of the 3rd circle
    turta.begin_fill()
    turta.circle(30)
    turta.end_fill()

def square(turta,square_color,border_color): #here is where turtle draws the square shape
    turta.fillcolor(square_color)
    turta.pencolor(border_color)

    setPostion(turta,-130,0) # position of the first square 
    turta.begin_fill()
    turta.forward(50) #the sqaure size
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.end_fill()

    setPostion(turta,-195,70) # postion of the 2nd square
    turta.begin_fill()
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.end_fill()

    setPostion(turta,-65,-70) # postion of the 3rd square
    turta.begin_fill()
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.forward(50)
    turta.left(90)
    turta.end_fill()

def hexagon(turta,hexa_color,border_color): #here is where turtle draws the hexagon shape
    turta.fillcolor(hexa_color)
    turta.pencolor(border_color)

    setPostion(turta,75,10) # postion of the 1st hexagon
    turta.begin_fill()# for the code to repeat 6 times
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.end_fill()

    setPostion(turta,10,80) # postion of the 2nd hexagon
    turta.begin_fill()
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.end_fill()

    setPostion(turta,130,-60) # postion of the 3rd hexagon
    turta.begin_fill()
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.forward(30)
    turta.left(60)
    turta.end_fill()

def pattern(turta, hexa_color, circle_color, square_color, border_color): # here is where we set each color
    turta.fillcolor(hexa_color)
    turta.fillcolor(circle_color)
    turta.fillcolor(square_color)
    turta.pencolor(border_color)


def main():
    circle_color = str(input("enter the color of the circle:")) # inputing the color 
    square_color = str(input("enter the color of the the square:")) # inputing the color
    hexa_color = str(input("enter the color of the the hexagon:")) # inputing the color
    pattern = str (input("enter the border of the shapes:")) # inputing the color
    circle(turtle,circle_color , pattern) 
    square(turtle, square_color, pattern)
    hexagon(turtle, hexa_color, pattern)
    input()

main()