#to print total marks and avg and its grade A,B ,C
name=input("enter the student name")
m1=int(input("enter m1 marks"))
m2=int(input("enter m2 marks"))
m3=int(input("enter m3 marks"))
total=m1+m2+m3
avg=(m1+m2+m3)/3
print("the total  marks and average marks of {0} is {1} and{2}:".format(name,total,avg))
if avg>=60:
    print("A grade")
elif avg<60 and avg>=45:
    print("B grade")
else:
    print("C grade")   