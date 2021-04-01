#check the number is divisible by 5 or not
a=int(input("enter the a value"))
if a%5==0:
    print("{0} is divisible by 5".format(a))
else:
    print("{0} is  not divisible by 5".format(a))


#using function
def div_by_5(a):
    if a%5==0:
        print("{0} is divisible by 5".format(a))
    else:
        print("{0} is  not divisible by 5".format(a))

div_by_5(96)