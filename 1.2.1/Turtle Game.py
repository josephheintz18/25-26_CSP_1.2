#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "lime"
score = 0


#-----initialize turtle-----
#The score turtle
score_writer = trtl.Turtle()
#The box turtle
box_turtle = trtl.Turtle()
#The timer turtle
counter = trtl.Turtle()
counter.hideturtle()
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False
score_writer.penup()
score_writer.hideturtle()
box_turtle.hideturtle()
pim = trtl.Turtle()
pim.shape("circle")
pim.color(spot_color)
pim.shapesize(3)
pim.penup()
box_turtle.speed(0)
score_writer.speed(0)

# -----game functions-----
def countdown():
    global timer, timer_up
    counter.clear()
    counter.penup()
    counter.goto(-375, 325)
    counter.pendown()
    if timer <= 0:
        counter.write("You're out of time bum!!", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

def scoreBox():
    # Set up the starting location and pendown
    box_turtle.penup()
    box_turtle.goto(275, 325)
    box_turtle.pendown()

    # Draw the box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)

    # Place score_writer where it will write the score
    box_turtle.penup()
    score_writer.goto(300, 332)

# Get a score boost, move the turtle randomly
def spot_clicked(x, y):
    change_position()

def change_position():
    # Move the turtle to a random location
    newX = rand.randint(-300, 300)
    newY = rand.randint(-300, 300)
    pim.goto(newX, newY)
    update_score()

def update_score():
    # Include the global score
    global score
    # Increment the score by 1
    score += 1
    score_writer.clear()
    # print the score
    score_writer.write(score, font=font_setup)

#-----events----------------
pim.onclick(spot_clicked)

scoreBox()
countdown()
wn = trtl.Screen()
wn.mainloop()