#to check whether its the number is armstrong or not
n=int(input("enter the value of n"))
result=0
x=len(str(n))
#temp=num
while n>0:
    result=0
    rem=n%10
    result=result+rem**x
    n=n/10
if n==result:
    print("the given number is an armstrong number")
else:
    print("not armstrong number")

