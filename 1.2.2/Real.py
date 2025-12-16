#-----import statements-----
import turtle as trtl
import random as rand
#import leaderboard as lb

#-----game configuration----
spot_color = "navy"
score = 0
font_setup = ("papyrus", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Enter your name?")

# Score turtle
score_writer = trtl.Turtle()
score_writer.penup()
counter =  trtl.Turtle()
counter.penup()

# Turtle to draw a box
box_turtle = trtl.Turtle()
box_turtle.penup()

# Shape turtle
pim = trtl.Turtle()
pim.shape("circle")
pim.color(spot_color)
pim.shapesize(3.5)
pim.penup()

#-----game functions--------
# Draw the box for the score
def scoreBox():
    # Set up the starting location and pendown
    box_turtle.goto(275, 325)
    box_turtle.pendown()

    # Draw the box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)

    # Place score_writer where it will write the score
    score_writer.penup()
    score_writer.goto(300, 332)

    # Hide the turtles
    score_writer.hideturtle()
    box_turtle.hideturtle()

# Get a score boost, move the turtle randomly
def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_position()
    else:
        pim.hideturtle()

def change_position():
    # Move the turtle to a random location
    pim.speed(0)
    newX = rand.randint(-300, 300)
    newY = rand.randint(-300, 300)
    pim.goto(newX, newY)
    update_score()

def update_score():
    # Include the global score
    global score
    # Increment the score by 1
    score += 1
    # Clear out the prior score
    score_writer.clear()
    # Print the current score
    score_writer.write(score, font=font_setup)

# Counter setup
def counter_setup():
    counter.forward(-200)
    counter.left(90)
    counter.forward(300)
    counter.right(90)
    counter.hideturtle()

# Start the countown and update it each frame
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up you bum", font=font_setup)
    timer_up = True
    manage_leaderboard()


  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# CODE TO ADD
# Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global moewl

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, moewl, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, moewl, score)


#-----events----------------
pim.onclick(spot_clicked)
counter_setup()
scoreBox()
wn = trtl.Screen()
wn.bgcolor("maroon")
wn.ontimer(countdown, counter_interval)
wn.mainloop()