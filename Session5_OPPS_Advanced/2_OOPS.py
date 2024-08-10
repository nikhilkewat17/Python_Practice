class Car:
    def __init__(self,model,make,color,power,mode):
        self.model = model
        self.make = make
        self.color = color
        self.power = power
        self.mode = mode
    def car_info(self):
        print("Car model : {}\nCar Make : {}\nCar Color : {}\nCar Power : {}\nCar mode : {}" \
              .format(self.model, self.make, self.color, self.power, self.mode))

        print("Welcome to '%s' , your car is '%s' & color is '%s' , horse power '%d' CC and your car is '%s' transformation ...! \n" \
              %(self.make,self.model,self.color,self.power,self.mode))

car1 = Car("Nexon","Tata","White",1199,"Manual")
car1.car_info()

car2 = Car("TUV-Neo","Mahindra","Black",1199,"Manual")
car2.car_info()

# car1 = Car()
# car1.model = "Nexon"
# car1.make = "Tata"
# car1.color = "White"
# car1.power = 1900
# car1.mode = "Manual"

# print("Car model : {}\nCar Make : {}\nCar Color : {}\nCar Power : {}\nCar mode {}"\
#       .format(car1.model,car1.make,car1.color,car1.power,car1.mode))
#
# car2 = Car()
# car2.model = "TUV-Neo"
# car2.make = "Mahindra"
# car2.color = "White"
# car2.power = 1999
# car2.mode = "Manual"
#
# print("Car model : {}\nCar Make : {}\nCar Color : {}\nCar Power : {}\nCar mode {}"\
#       .format(car2.model,car2.make,car2.color,car2.power,car2.mode))


