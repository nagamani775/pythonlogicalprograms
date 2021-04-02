#class employee management
class Employee:

    def __init__(self,ename,eno,esal):
        self.ename=ename
        self.eno=eno
        self.esal=esal

    def info(self):
        print("Employee details are:")
        print("ename is:",self.ename)
        print("eno is:",self.eno)
        print("esal is:",self.esal)

    def m1(self):
        del self.ename,self.eno,self.esal
        print("Employee details can be deleted successfully")

    def modify(self):
        ename=input("enter updated Employee name:")
        eno=int(input("enter updated Employee number is:"))
        esal=int(input("enter updated Employee salary is:"))
        print("Employee updated details are:")
        print("ename:",ename)
        print("eno :",eno)
        print("esal is:",esal)
        print("Employee details updated successfully")

n=int(input("enter number of Employees:"))
for i in range(n):
    ename=input("enter name:")
    eno=int(input("enter eno:"))
    esal=int(input("enter esalary"))
    e=Employee(ename,eno,esal)
    e.info()
    e.modify()
    e.m1()
    print(e.__dict__)
