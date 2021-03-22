#accept employee information and reprint it

class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def information(self):
        print("name:",self.name)
        print("emp_id:",self.emp_id)
        print("salary:",self.salary)
e=Employee('mani',498,50000)
e.information()