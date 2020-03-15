from turtle import forward, left, right, shape, exitonclick, penup, pendown
import math
shape('turtle')

for i in range(5):
    forward(200/5)
    left(180-(180*(1-2/5)))

penup()
forward(100)
pendown()

for i in range(6):
    forward(200/6)
    left(180-(180*(1-2/6)))

penup()
forward(100)
pendown()

for i in range(7):
    forward(200/7)
    left(180-(180*(1-2/7)))

penup()
forward(100)
pendown()

for i in range(8):
    forward(200/8)
    left(180-(180*(1-2/8)))

penup()
forward(100)
pendown()

n = int(input('Zadej cele kladne cislo: '))

for i in range(n):
    forward(200/n)
    left(180-(180*(1-2/n))) 

penup()
forward(100)
pendown()

for i in range(360):
    forward(200/360)
    left(180-(180*(1-2/360))) 

penup()
forward(100)
pendown()

for i in range(95):
    forward(200/95)
    left(180-(180*(1-2/95))) 

exitonclick()