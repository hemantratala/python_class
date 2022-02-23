class employee:
    def __init__(self,name,salary,taxpercent):
        self.name=name
        self.salary=salary
        self.taxpercent=taxpercent
    def netsalary(self):
        salaryaftertax=self.salary-self.salary*self.taxpercent
        return salaryaftertax
employee1= employee("hemant",25000,0.01)
employee2= employee("sumit",30000,0.01)
employee3= employee("surya",70000,0.01)
print(employee1.netsalary())
print(employee2.netsalary())
print(employee3.netsalary())