class student:
    def __init__(self):
        self.name = ""
        self.major = ""
        self.gpa = 0

        # display object atteibute
    def student_info(self):
            print(f'name:{self.name} major:{self.major} GPA:{self.gpa}')



s1 = student()
# adding data to object attribute
s1.name = "mork"
s1.major = "mit"
s1.gpa = 3.0

# display student data
s1.student_info()

# get data from user
# s2 = student()
# s2.name = input("Enter name:")
# s2.major = input("Enter major:")
# s2.gpa = input("Enter GPA:")
# s2.student_info()

std = []

n = int(input('How many student : '))
for i in range(n):
    s = student()
    s.name = input(f"please, Enter studeut info{i+1}:")
    s.major = input("Enter major:")
    s.gpa = float(input("Enter GPA:"))
    s.student_info()
    std.append(s)

# display all student in list
for i in std:
    i.student_info()
