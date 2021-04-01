#to pint square and cube of numbes
a=int(input("enter the a value"))
print("the square is:",a*a)
print("the cube is:",a**3)

#using function
def square(a):
    b=a*a
    return b
def cube(x):
    y=x**3
    return y

print(square(4))
print(cube(2))