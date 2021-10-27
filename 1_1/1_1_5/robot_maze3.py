#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

i = 0
while (i < 1): # forward 1
  move()
  i = i + 1 

m=0
while (m < 3): #turn left
   turn_left()
   m=m+1

n = 0
while (n < 2): # forward 2
  move()
  n = n + 1 

k=0
while (k < 1): #turn left
   turn_left()
   k=k+1

c=0
while (c < 2): #forward 2
  move()
  c=c+1

l=0
while (l < 3): #turn lefy
  turn_left()
  l=l+1

g=0
while (g < 2): #forward 2
  move()
  g=g+1

b=0
while (b < 1): #turn left
  turn_left()
  b=b+1

d=0
while (d < 1): #forward 1
  move()
  d=d+1

#---- end robot movement 

wn.mainloop()