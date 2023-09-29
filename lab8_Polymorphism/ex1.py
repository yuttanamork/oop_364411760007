class person():
    def __init__(self):
        # list of attributes
        self.name = ""
        self.age = 0
        self.gender = ""

    def info(self):
        print(f'name : {self.name} age: {self.age} gender: {self.gender} ')

class employee():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.emp_id = ""
        self.position = ""

    def info(self):
        print(f'name : {self.name} '
              f'age: {self.age} '
              f'gender: {self.gender}'
              f'emp_id: {self.emp_id} ' 
              f'position: {self.position}')



p1 = person()
p1.name = "yuttana datmark"
p1.age = 24
p1.gender = "male"

emp1 = employee()
emp1.name = "bank"
emp1.age = 10
emp1.gender = "male"
emp1.emp_id = "mit431"
emp1.position = "lecturer"



p1.info()
emp1.info()


lst = [p1,emp1]

for obj in lst:
    print(obj.__class__.__name__, end=" ")
    obj.info()

class student():
    def __init__(self):
        # list of attributes
        self.name = ""
        self.age = 0
        self.gender = ""
        self.student_id = 0
        self.major = ""
        self.university = ""


    def info(self):
        print(f'name : {self.name} '
              f'age: {self.age} '
              f'gender: {self.gender}'
              f'student_id: {self.student_id}'
              f'major: {self.major}'
              f'university: {self.university}')


s1 = student()
s1.name = "yuttana datmark"
s1.age = "24"
s1.gender = "male"
s1.student_id = "364411760007"
s1.major = "mit"
s1.university = "rmuts"

s1.info()
lst = [s1]
for obj in lst:
    print(obj.__class__.__name__, end=" ")
    obj.info()