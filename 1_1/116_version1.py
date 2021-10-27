#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider_body is used
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)

spider_legs = 6
spider_leg_length=70
spider_leg_angle = 380 / spider_legs

print("spider_leg_angle",spider_leg_angle)

spider_body.pensize(5)
loops = 0
while (loops < spider_legs):
  spider_body.goto(0,0)
  spider_body.setheading(spider_leg_angle*loops)
  spider_body.forward(spider_leg_length)
  loops = loops + 1
spider_body.hideturtle()
print("spider_leg_angle*n=",spider_leg_angle*loops)

wn = trtl.Screen()
wn.mainloop()