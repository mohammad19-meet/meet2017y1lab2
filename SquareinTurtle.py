import turtle
turtle.penup()​ ​ #Pick up the pen so it doesn’t draw
turtle.goto(-200,-100)​ ​ #Move the turtle to the
#position, -200, -100, on
#the screen
turtle.pendown()​ ​ #Put the pen down to start
#drawing
#Draw the square:
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
# ...and end it before the next line.
turtle.mainloop()
