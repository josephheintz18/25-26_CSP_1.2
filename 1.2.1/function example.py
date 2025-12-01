#Import turtle
import turtle as trtl

#Make a turtle
james = trtl.Turtle()

#Goal: Draw squares with a turtle
def drawSquare():
    for sides in range(4):
        james.forward(100)
        james.right(90)

drawSquare()
james.penup()
james.forward(200)
james.pendown()
drawSquare()


wn = trtl.Screen()
wn.mainloop()