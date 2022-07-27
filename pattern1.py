from turtle import *
speed('fastest')
pencolor('yellow')
pensize(3)
bgcolor('black')

for i in range(100):
    backward(i)
    left(60)
    circle(i)
    

mainloop()