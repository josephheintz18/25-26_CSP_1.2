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

#   a123_apple_and_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty.

#TODO Create a function that draws a new letter from the letter list.

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter
# to disappear. Call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.onkeypress(drop_apple, "a")

wn.listen()
trtl.mainloop()