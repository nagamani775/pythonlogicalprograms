#lengthh of the string
s=input("enter string")
l=len(s)
print("the length of the string is:",l)

#using function

def findlen(str):
    counter=0
    for s in str:
        counter=counter+1
    return counter


findlen('mani')
print(findlen('mani'))