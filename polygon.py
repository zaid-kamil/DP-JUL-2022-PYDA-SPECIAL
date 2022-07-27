from turtle import *

side = int(input("how many side for your polygon = "))
size = int(input('size of 1 side in px = '))

for i in range(side):
    forward(size)
    left(360/side)
    dot(20,'blue')
mainloop()
