#to find quadratic equations
from cmath import sqrt
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
d=(b**2)-(4*a*c)
q1=(-b + sqrt(d))/(2*a)
q2=(-b - sqrt(d))/(2*a)

print("the quadratic equations are:",q1,q2)
