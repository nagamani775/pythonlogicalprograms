#employee management system using setter and getter methods
class Employee:
    def _init__(self,ename,eno,esal):
        self.ename=ename
        self.eno=eno
        self.esal=esal

    def set(self,ename,eno,esal):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        

    def get(self):
        return self.ename,self.eno,self.esal

n=int(input("enter no.of students:"))
for i in range(n):
    e=Employee()
    ename=input("enter Employee name:")
    eno=int(input("enter Employee number"))
    esal=int(input("enter Employee salary"))
    e.set(ename,eno,esal)

    print("Details are",e.get())
