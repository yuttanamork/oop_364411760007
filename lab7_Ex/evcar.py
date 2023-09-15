class Thaievcar:
    ev_car_detail = []

    def __init__(self,id,model,brand,accelerationrate,hp,range,price):
        self.__id = id
        self.__model = model
        self.__brand = brand
        self.__accelerationrate = accelerationrate
        self.__hp = hp
        self.__range = range
        self.__price = price

    def Thaievcar_info(self):
        print(f'id:{self.__id} '
              f'model:{self.__model} '
              f'brand:{self.__brand} '
              f'accelerationrate:{self.__accelerationrate} '
              f'hp:{self.__hp} '
              f'range:{self.__range} '
              f'price:{self.__price} ')


    #getter and setter methods
    def get_id(self):
        return self.__id

    def get_model(self):
        return self.__model
    def set_model(self,new_model):# update data in attribute
        self.__model = new_model

    def get_brand(self):
        return self.__brand
    def set_brand(self,new_brand):# update data in attribute
        self.__brand = new_brand

    def get_accelerationrate(self):
        return self.__accelerationrate
    def set_accelerationrate(self,new_accelerationrate):# update data in attribute
        self.__accelerationrate = new_accelerationrate

    def get_hp(self):
        return self.__hp
    def set_hp(self,new_hp):# update data in attribute
        self.__hp = new_hp

    def get_range(self):
            return self.__range
    def set_range(self, new_range):  # update data in attribute
            self.__range = new_range

    def get_price(self):
            return self.__price
    def set_price(self, new_price):  # update data in attribute
            self.__price = new_price



