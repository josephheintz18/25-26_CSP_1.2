#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()
ground_height= (-200,0)
drawer.hideturtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_an_A():
  drawer.color("violet")
  drawer.write("A", font=("Arial", 74, "bold"))

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
    apple.goto(apple.xcor(), ground_height)

#-----function calls-----
wn.onkeypress(draw_an_A, "a")

if wn.onkeypress(draw_an_A, "a"):
    apple.right(90)
    apple.forward(90000)

wn.listen()

draw_apple(apple)

wn.mainloop()