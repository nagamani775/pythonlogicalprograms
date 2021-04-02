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


e=Employee('mishika',344,5000)
e1=Employee('swathi',498,20000)
e2=Employee('mani',455,30000)
e3=Employee('renu',566,4000)
e.info()
e1.m1()
print(e1.__dict__)
e2.info()
e3.modify()
