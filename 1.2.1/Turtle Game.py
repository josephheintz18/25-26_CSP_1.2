import turtle as trtl
import random as rand

#-----game configuration----
color = "purple"

#-----initialize turtle-----
pim = trtl.Turtle()
pim.shape("circle")
pim.color(color)
pim.shapesize(3)

#-----game functions--------
# Get a score boost, move the turtle around randomly
def spot_clicked(x,y):
    print("Mediocre job!")
    pim.penup()
    good_x = rand.randint(0,400)
    good_y = rand.randint(0, 400)
    pim.goto(good_x,good_y)
    pim.pendown()

#-----events----------------
pim.onclick(spot_clicked)

#loop for gameplay


#Set up the screen
wn = trtl.Screen()
wn.mainloop()