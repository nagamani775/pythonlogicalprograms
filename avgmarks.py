#to accept student name and 3 marks and finds its average
name=input("enter the name")
m1=int(input("enter m1 marks"))
m2=int(input("enter m2 marks"))
m3=int(input("enter m3marks"))
avg=(m1+m2+m3)/3
print("the average marks of {0} is {1}".format(name,avg))


#using funtion

def avg(name,m1,m2,m3):
    a=(m1+m2+m3)/3
    return a

print(avg('mishika',80,90,75))
