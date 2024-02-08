import turtle

def setPostion(turta,x,y):
    turta.penup()
    turta.goto(x,y)
    turta.pendown()

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

def main():
    square(turtle,'blue','red')

main()