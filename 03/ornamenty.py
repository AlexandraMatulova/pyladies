from turtle import forward, left, right, shape, exitonclick, penup, pendown
import math
shape('turtle')

'''
for i in range(20):
    forward(5*i)
    left(90)

penup()
right(90)
forward(200)
pendown()

for i in range(40):
    forward(i)
    left(45) 

penup()
right(90)
forward(200)
pendown()
'''


for i in range(1000):
    forward(0.002*i)
    left(1)

exitonclick()
