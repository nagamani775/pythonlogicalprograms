#to print the area of the circle
from math import pi
r=int(input("enter the radius"))
area=pi*r*r
print("the area of circle is:",area)

#using function
from math import pi
def area(r):
    a=pi*r*r
    return a
r=int(input("radius"))
print(area(r))