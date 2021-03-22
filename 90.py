#remove duplicates from the string
str1=input("enter string")
I=[]
for x in str1:
    if x not in I:
        I.append(x)
output="".join(I)
print(output)