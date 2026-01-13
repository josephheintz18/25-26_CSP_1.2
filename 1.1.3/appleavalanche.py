import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
current_letter = "a"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


wn.bgpic("background.gif")
apple = trtl.Turtle()
wn.tracer(False)
apple.penup()

def reset_apple(active_apple):
    # Generate a random number - > pop that index
    # The letter we pop, becomes the letter on the apple
    global current_letter
    length_of_list = len(letters)
    if(length_of_list != 0):
        index = rand.randint(0, length_of_list)
        current_letter = letters.pop(index)
        # Finish This First
        active_apple.goto(200, 200)
        draw_apple(active_apple, current_letter)


# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, current_letter):
  active_apple.shape(apple_image)
  #Show Turtle Here
  active_apple.showturtle()
  draw_letter(current_letter, active_apple)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("papyrus", 74, "bold"))
  active_apple.setpos(remember_position)

draw_apple(apple, current_letter)


#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.



#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.



#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.onkeypress(drop_apple, current_letter)

def check_apple_a():
    if(current_letter == "a"):
        drop_apple()

def check_apple_b():
    if(current_letter == "b"):
        drop_apple()

def check_apple_c():
    if(current_letter == "c"):
        drop_apple()

def check_apple_d():
    if(current_letter == "d"):
        drop_apple()

def check_apple_e():
    if(current_letter == "e"):
        drop_apple()

def check_apple_f():
    if(current_letter == "f"):
        drop_apple()

def check_apple_g():
    if(current_letter == "g"):
        drop_apple()

def check_apple_h():
    if(current_letter == "h"):
        drop_apple()

def check_apple_i():
    if(current_letter == "i"):
        drop_apple()

def check_apple_j():
    if(current_letter == "j"):
        drop_apple()

def check_apple_k():
    if(current_letter == "k"):
        drop_apple()

def check_apple_l():
    if(current_letter == "l"):
        drop_apple()

def check_apple_m():
    if(current_letter == "m"):
        drop_apple()

def check_apple_n():
    if(current_letter == "n"):
        drop_apple()

def check_apple_o():
    if(current_letter == "o"):
        drop_apple()

def check_apple_p():
    if(current_letter == "p"):
        drop_apple()

def check_apple_q():
    if(current_letter == "q"):
        drop_apple()

def check_apple_r():
    if(current_letter == "r"):
        drop_apple()

def check_apple_s():
    if(current_letter == "s"):
        drop_apple()

def check_apple_t():
    if(current_letter == "t"):
        drop_apple()

def check_apple_u():
    if(current_letter == "u"):
        drop_apple()

def check_apple_v():
    if(current_letter == "v"):
        drop_apple()

def check_apple_w():
    if(current_letter == "w"):
        drop_apple()

def check_apple_x():
    if(current_letter == "x"):
        drop_apple()

def check_apple_y():
    if(current_letter == "y"):
        drop_apple()

def check_apple_z():
    if(current_letter == "z"):
        drop_apple()


draw_apple(apple, current_letter)

wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_e, "e")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_i, "i")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_m, "m")
wn.onkeypress(check_apple_n, "n")
wn.onkeypress(check_apple_o, "o")
wn.onkeypress(check_apple_p, "p")
wn.onkeypress(check_apple_q, "q")
wn.onkeypress(check_apple_r, "r")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_t, "t")
wn.onkeypress(check_apple_u, "u")
wn.onkeypress(check_apple_v, "v")
wn.onkeypress(check_apple_w, "w")
wn.onkeypress(check_apple_x, "x")
wn.onkeypress(check_apple_y, "y")
wn.onkeypress(check_apple_z, "z")

wn.listen()
trtl.mainloop()