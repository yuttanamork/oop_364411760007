from oopExerciseChapter6 import vehicle

def display_option():
    print("Welcome to Vehicle Data Stoer System(VDSS)")
    print("1.Add Vehicle")
    print("2.delete vehicle")
    print("3.edit vehicle price")
    print("4.edit vehicle color")
    print("5.Display all Vehicle")
    print("6.exit")


    select = int(input("select(1-6)? : "))
    if select == 1:
        input_vehicle_info()
    elif select == 2:
        delete_vehicle()
    elif select == 3:
        edit_vehicle_price()
    elif select == 4:
        edit_vehicle_color()
    elif select == 5:
        display_vehicle()
    elif select == 6:
        print("Good Bye")
        exit(0)
    else:
        print("Please, select number 1-6")

def input_vehicle_info():
    brand = input("Enter vehicle brand ")
    model = input("Enter vehicle model")
    color = input("Enter vehicle color")
    maxspeed = int(input("Enter vehicle maxspeed:"))
    price = float(input("Enter vehicle price:"))

    vehicle.my_vehicle.append(vehicle(brand,model,color,maxspeed,price))
    print("\n-----------------------")
    print("Already add vehicle to stoer")
    print("-----------------\n")

def display_vehicle():
    if len(vehicle.my_vehicle) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had{len(vehicle.my_vehicle)} following:')
        n = 1 #count
        for x in vehicle.my_vehicle:
            print(f'[{n}]:',end=" ")
            n = n+1
            x.vehicle_info()
        print("\n")

#delete vehicle
def delete_vehicle():
    display_vehicle()
    if len(vehicle.my_vehicle) != 0:

        s = int(input("select to delete"))
        vehicle.delete_vehicle(vehicle,s-1)
        print("\n----------------------------")
        print("your data has been delete")
        print("----------------------------\n")

def edit_vehicle_price():
    display_vehicle()
    if len (vehicle.my_vehicle) != 0:
        s = int(input("select to edit? : "))
        print(f'\nprevious price: {vehicle.my_vehicle[s-1].price}')
        new_price = float(input("new price:"))
        vehicle.edit_vehicle_price(vehicle,s-1,new_price)
        print("\n----------------------------")
        print("your data has been delete")
        print("----------------------------\n")

def edit_vehicle_color():
    display_vehicle()
    if len (vehicle.my_vehicle) != 0:
        s = int(input("select to edit? : "))
        print(f'\nprevious price: {vehicle.my_vehicle[s-1].color}')
        new_color = input("new color:")
        vehicle.edit_vehicle_color(vehicle,s-1,new_color)
        print("\n----------------------------")
        print("your data has been delete")
        print("----------------------------\n")



#my_vehicle = []
s = 0
while s == 0:
    display_option()









