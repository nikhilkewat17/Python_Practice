class Vehicle:
    def general_usage(self):
        print("Transport")
class Car(Vehicle):
    def general_usage_car(self):
        print("Travel to Nature in world wide")
class Truck(Vehicle):
    def general_usage_truck(self):
        print("Transfer the big items")

car=Car()
truck= Truck()

car.general_usage()
car.general_usage_car()

truck.general_usage()
truck.general_usage_truck()

