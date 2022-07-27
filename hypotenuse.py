import math

p = float(input("Perpendicular: "))
b = float(input("Base: "))
h = math.hypot(p, b)
print(f"Hypotenuse: {h}")