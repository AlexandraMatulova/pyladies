from turtle import forward, left, right, shape, exitonclick, penup, pendown, setx, sety
import random
shape('turtle')

penup()
right(90)
forward(300)
right(90)
forward(300)
right(180)
pendown()

#panelaky
for i in range(3):
    forward(30)
    left(90)
    forward(150)
    right(90)
    forward(70)
    right(90)
    forward(150)
    left(90)
    forward(40)
    left(90)
    forward(90)
    right(90)
    forward(60)
    right(90)
    forward(90)
    left(90)
    forward(30)

#okna
penup()
left(180)
for i in range(3):
    forward(35)
    right(90)
    forward(80)
    left(90)
    for i in range(6):
        for i in range(2):
            pendown()
            forward(5)
            left(90)
            forward(10)
            left(90)
        penup()
        forward(10)
    forward(40)
    right(90)
    forward(40)
    left(90)
    for i in range(6):
        for i in range(2):
            pendown()
            forward(7)
            left(90)
            forward(15)
            left(90)
        penup()
        forward(10)
    left(180)
    forward(60)
    right(90)
    forward(40)
    right(90)
    for i in range(6):
        for i in range(2):
            pendown()
            forward(7)
            left(90)
            forward(15)
            left(90)
        penup()
        forward(10)
    left(90)
    forward(90)
    right(90)
    forward(35)

#hvezdy
for i in range(20):
    penup()
    setx(random.randint(-300,400))
    sety(random.randint(-100,100))
    pendown()
    for i in range(6):
        forward(20)
        left(180)
        forward(20)
        left(120)

exitonclick()