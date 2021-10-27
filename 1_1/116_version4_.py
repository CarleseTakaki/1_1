#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider_body is used
spider_body = trtl.Turtle()
spider_body.pensize(40)

#create spider body
spider_body.circle(20)

#configure spider legs
spider_legs = 8
spider_leg_length=70
spider_leg_angle = 300 / spider_legs

print("spider_leg_angle",spider_leg_angle)

#draw legs
spider_body.pensize(5)
loops = 0
while (loops < spider_legs):
  spider_body.goto(0,20)
  spider_body.setheading(spider_leg_angle*loops-45)
  spider_body.forward(spider_leg_length)
  loops = loops + 1
spider_body.hideturtle()
print("spider_leg_angle*n=",spider_leg_angle*loops)

def spider_eyes():
  spider_body.color("orange")
  spider_body.begin_fill()
  spider_body.circle(4)
  spider_body.end_fill()

for i in range(2):
  spider_body.penup()
  spider_body.goto(-10,0)
  spider_body.pendown()
  spider_eyes()
  spider_body.penup()
  spider_body.goto(4,0)
  spider_body.pendown()
  spider_eyes()



wn = trtl.Screen()
wn.mainloop()