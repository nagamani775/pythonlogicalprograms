#to print area of the triangle
b=6
h=12
area=0.5*b*h
print("the area of the triangle is:",area)

#using function
def area(b,h):
    a=0.5*b*h
    return a
b=int(input("breath"))
h=int(input("height"))

print(area(b,h))

#using function using print
def area(b,h):
    a=0.5*b*h
    print(a)


area(4,3)