#Import turtle
import turtle as trtl

#Make a turtle
james = trtl.Turtle()

#Goal: Draw squares with a turtle
def drawSquare(length):
    for sides in range(4):
        james.forward(length)
        james.right(90)

drawSquare(62)
james.penup()
james.forward(-200)
james.pendown()
drawSquare(47)


wn = trtl.Screen()
wn.mainloop()