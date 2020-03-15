from turtle import forward, left, right, shape, exitonclick, penup, pendown
import math
shape('turtle')

for j in range(10):
    for i in range(4):
        forward(50)
        left(90)
    left(45)
    forward(math.sqrt(2)*50)
    left(135)
    penup()
    forward(50)
    left(135)
    pendown()
    forward(math.sqrt(2)*50)
    left(135)
    penup()
    forward(50)
    left(45)
    pendown()
    forward(math.sqrt(2)*50/2)
    left(90)
    forward(math.sqrt(2)*50/2)
    left(45)
    penup()
    forward(50)
    left(90)
    forward(50)
    pendown()
    forward(10)

exitonclick()