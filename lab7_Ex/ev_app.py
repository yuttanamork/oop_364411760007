from evcar import Thaievcar

def display_option():
    print("1.Add ev car")
    print("2.display all ev car")
    print("3.exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        add_ev_car()
    elif select == 2:
        display_ev_car()
    elif select == 3:
        print("Good Bye")
        exit(0)
    else:
        print("Please, select number 1-3")

def add_ev_car():
    __id = input("carid:")
    __model = input("กรุณากรอกรุ่นรถ! : ")
    __brand = input("กรุณากรอกยี่ห้อรถ!: ")
    __accelerationrat = input("กรุณากรอกอัตราเร่งรถ!: ")
    __hp = input("กรุณากรอกแรงม้ารถ!: ")
    __range = input("กรุณากรอกระยะทางที่รถวิ่งได้/ชาร์จ!: ")
    __price = float(input("กรุณากรอกราคารถ! : "))

    Thaievcar.ev_car_detail.append(Thaievcar(__id,__model,__brand,__accelerationrat,__hp,__range,__price,))
    print("\n--------------------------------------")
    print("ทำการเพิ่มข้อมูลรถเรียบร้อยแล้ว.")
    print("--------------------------------------\n")

def display_ev_car():
    if len(Thaievcar.ev_car_detail) ==0:
        print("ไม่มีข้อมูลรถให้แสดง! .")
    else:
        print(f'คุณมี {len(Thaievcar.ev_car_detail)} following')
        n = 1001 # count
        for x in Thaievcar.ev_car_detail:
            print(f'[{n}]:' ,end=" ")
            x.Thaievcar_info()
            n = n+1001
        print("\n")

s = 0
while s == 0:
    display_option()