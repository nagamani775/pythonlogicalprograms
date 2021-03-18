#swap two nnumbers using functions
def swap(a,b):
    print("before swapping:",a,b)
    temp=a
    a=b
    b=temp
    print("before swapping:",a,b)

a=int(input("enter a value"))
b=int(input("enter b value"))
swap(a,b)