#print string and copy to another variable,length,lower ,uppercases
str1=input("enter input string")
r=reversed(str1)
output=''.join(r)
print("reversed string is:",output)
l=len(str1)
print("length is:",l)
u=str1.upper()
print("upper is:",u)
lowr=str1.lower()
print("lower is:",lowr)
str2=str1
print("copied strinng is:",str2)