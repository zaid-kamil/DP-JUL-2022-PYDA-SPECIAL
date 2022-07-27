from turtle import *

def polygon(side,size=50):
    for i in range(side):
        forward(size)
        left(360/side)

def pentagon(size=50):
    fillcolor('red')
    begin_fill()
    polygon(5,size)
    end_fill()

def triangle(size=50):
    fillcolor('yellow')
    begin_fill()
    polygon(3,size)
    end_fill()

def octagon(size=50):
    fillcolor('#89898f')
    begin_fill()
    polygon(8,size)
    end_fill()

speed(0)

for i in range(200):
    if i % 2==0:
        pentagon(30)
    else:
        octagon(10)
    forward(i+20)
    left(60)

mainloop()