#Empoyee management system

class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def get(self,id):
        if id in e:
            print("id of {0} details are:".format(id))
        else:
            print("this number not available")
        print("id:",self.id)

        print("name:",self.name)
        print("sal:",self.sal)
    def des(self):
        if id in e:
            print("id of {0} details are:".format(id))
        else:
            print("this number not available")
        del self.id,self.name,self.sal
        print("{0} details deleted successfully".format(id))
    def update(self):
        if id in e:
            print("id of {0} details are:".format(id))
        else:
            print("this number not available")
        name=input("enter updated Employee name")
        sal=int(input("enter updated salary"))
        print("updated name:",name)
        print("updated salary:",sal)
        print(" {0} details are updated successfully:".format(id))
n=int(input("enter employee numbers"))
for i in range(n):
    id=int(input("enter id:"))
    name=input("enter name")
    sal=int(input("enter salary:"))
e=Employee(id,name,sal)
while True:
    print('g-get \nd-des \nu-update')
    option=input("choose your option:")
    if option=='g' or option=='G':
        id=int(input("enter id number you have to get"))
        e.get(id)
    elif option=='d' or option=='D':
        id=int(input("enter id number you have to delete"))
        e.des()
    elif option=='u' or option=='U':
        id=int(input("enter id number you have to updated"))
        e.update()
    else:
        print(" plz choose valid option")


