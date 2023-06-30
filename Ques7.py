# Ques: Python Program for Program to find area of a circle
# Area = pi * r2
# where r is radius of circle 
import math

r = int(input("Please enter a valid radius od a circle:"))

a = math.pi * pow(r, 2)

print(f"area: {a}")