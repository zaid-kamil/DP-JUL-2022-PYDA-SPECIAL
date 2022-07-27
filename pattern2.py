from turtle import *
speed('fastest')
pencolor('yellow')
pensize(1)
bgcolor('black')

for i in range(100):
    backward(i)
    left(360/6)
    # inner loop
    for j in range(5):
        forward(i)
        left(360/5)
    

mainloop()