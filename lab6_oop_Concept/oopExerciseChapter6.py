class vehicle:
    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price



        # display object atteibute
    def vehicle_info(self):
            print(f'brand:{self.brand} '
                  f'model:{self.model} '
                  f'color:{self.color} '
                  f'maxspeed:{self.maxspeed} '
                  f'price:{self.price}')
# std = []
# n = int(input('How many Vehicle : '))
# for i in range(n):
#
#     s = Vehicle()
#     print(f"please, Enter brand info:")
#     s.brand = input("Enter brand:")
#     s.model = input("Enter model:")
#     s.color = input("Enter color:")
#     s.maxspeed = input("Enter maxspeed:")
#     s.price = input("Enter price:")
#     std.append(s)
#
# for i in std:
#     i.Vehicle_info()

