import turtle

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

def main():
    circle(turtle,'blue', 'red')

main()