class notbook:
    def __init__(self):
        self.cpu = ""
        self.gpu = ""
        self.ram = 0
        self.display = 0
        self.STORAGE = 0
        self.os = 0


        # display object atteibute
    def notbook_info(self):
            print(f'cpu:{self.cpu} gpu:{self.gpu} ram:{self.ram} display:{self.display} STORAGE:{self.STORAGE}  os:{self.os} ')

std = []

n = int(input('How many notbook : '))
for i in range(n):
    s = notbook()
    print(f"please, Enter cpu info{i+1}:")
    s.gpu = input("Enter cpu:")
    s.gpu = input("Enter gpu:")
    s.ram = input("Enter ram:")
    s.display = input("Enter display:")
    s.STORAGE = input("Enter STORAGE:")
    s.os = input("Enter os:")
    std.append(s)

for i in std:
    i.notbook_info()