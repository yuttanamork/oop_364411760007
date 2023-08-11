
# class creation
class Student:
    # class attribute
    faculty = "MT"
    # init method
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


# display object atteibute
    def student_info(self):
        print(f'name:{self.name} major:{self.major} GPA:{self.gpa}')





#  object creation
s1 = Student("Mork" , "MIT", 3.00)
s2 = Student("Bass" , "DBM", 3.55)
# S3 = Student()

# display attributes objiect
print(s1.name, s1.major, s1.gpa)
print(s2.name, s2.major, s2.gpa)

# display with f-string
print(f'name:{s1.name} major:{s1.major} GPA:{s1.gpa}')
print(f'name:{s2.name} major:{s2.major} GPA:{s2.gpa}')


print(s1.faculty, s2.faculty)

# change data in object atteibute
print(s1.major)
s1.major = "MG"
print(s1.major)

# obect call method in class
s1.student_info()
s2.student_info()

# List
std_list = []   # std_list = [s1,s2]
std_list.append(s1)
std_list.append(s2)
# display number object in list
print(len(std_list))

# for loop and list
for x in std_list:
    x.student_info()


