class employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def employ_info(self):
        print(f'employee name : {self.name} salary b: {self.__salary}')

    #getter and setter methods
    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):# update data in attribute
        self.__salary = new_salary



emp = employee("yuttana",10000)
emp.employ_info()

# access to pudlic member
print(emp.name)
#print(emp.__salary)

#name mangling
print(emp._employee__salary)

#call to gatter and setter method
print(emp.get_salary())
emp.set_salary(20000)
emp.employ_info()