import turtle as trtl

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -800
apple_letter_x_offset = -25
apple_letter_y_offset = -50

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("background.gif")
apple = trtl.Turtle()
drawer = trtl.Turtle()
drawer.hideturtle()
apple.penup()

#Make list for letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.tracer(False)
  draw_letter("A", active_apple)
  wn.tracer(True)

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  wn.tracer(False)
  drawer.clear()
  drawer.hideturtle()

def draw_letter(letter, drawer):
  drawer.color("white")
  remember_position = drawer.position()
  drawer.setpos(drawer.xcor() + apple_letter_x_offset,drawer.ycor() + apple_letter_y_offset)
  drawer.write(letter, font=("Arial", 74, "bold"))
  drawer.setpos(remember_position)

draw_apple(apple)
wn.onkeypress(drop_apple, "a")

wn.listen()
trtl.mainloop()