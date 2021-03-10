#to print gender and its age to check he/she eligible for marriage or not
name=input("enter the name")
age=int(input("enter the age"))
if age>=18:
    print("{0} is eligible for marrige".format(name))
else:
    print("{0} is not eligible for marrige".format(name))
