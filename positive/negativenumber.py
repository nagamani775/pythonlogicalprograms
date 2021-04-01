#to print wheather the number is +ve or -ve
a=int(input("enter the a value"))
if a>=0:
    print("the number is a +ve number")
else:
    print("the number is a -ve number")

#using function
def pos_neg(a):
    if a>=0:
        print("the number is a +ve number")
    else:
        print("the number is a -ve number")

pos_neg(-10)