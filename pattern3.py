from turtle import *

for i in range(6):
    if i % 3 == 0:
        color('red')
    elif i % 3 == 1:
        color('green')
    else:
        color('blue')
    forward(100)
    left(360/6)
mainloop()