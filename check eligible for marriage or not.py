#to print gender and its age to check he/she eligible for marriage or not

def eligible(name,age):
    if age>=18:
        print("{0} is eligible for marrige".format(name))
    else:
        print("{0} is not eligible for marrige".format(name))
#name=input("enter the name")
#age=int(input("enter the age"))

eligible('swathi',20)
eligible('renu',15)

