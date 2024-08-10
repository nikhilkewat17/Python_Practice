class Car:
    def __init__(self,model,make,color,power,mode,):
        self.model = model
        self.make = make
        self.color = color
        self.power = power
        self.mode = mode
        self.mileage = 0
    def car_info(self):
        print("Welcome to our Showroom You choose '%s' car manufacturer by '%s' and color is '%s' , power of this car is '%d' and transmition is '%s' mode ...!"\
              %(self.model,self.make,self.color,self.power,self.mode))
    def update_mileage(self,miles):
        if miles >= self.mileage :
            self.mileage = miles
        else:
            print("Error: Mileage cannot decrease")
car1 = Car("Nexon","TATA","Balck",1199,"Manual")

car1.car_info()
car1.update_mileage(26)
print("Your car mileage is %d ...!" %(car1.mileage))

# Explanation:

# - Class: `Car` is a class, which is like a blueprint for creating objects (instances).
# - Attributes:
#   - `make`, `model`, and `year` are attributes stored within each `Car` object.
#      They define the characteristics of the car.
#   - `mileage` is an additional attribute used to track the car's mileage.

# - Methods:
#   - `describe()` is a method that uses the car's attributes to return a formatted string
#      describing the car.
#   - `update_mileage(miles)` is a method to update the car's mileage. It includes a check
#      to ensure that mileage does not decrease.

# - Instances: `my_car` is an instance of the `Car` class, representing a specific car.
#   - `__init__()`: This special method is called the initializer. It initializes new
#     instances of the class. It's automatically invoked when a new object is created.
#   - `self`: It refers to the current instance of the class. It is used to access variables
#      that belong to the class. It must be the first parameter of any method in the class.


# Study Drills :
# 1. Try creating class without init method
# 2. Create class with init method, find out the difference
# 3. Print Car details manually, later create function to display car details
# 4. Try to run display method without self
# 5. Try to call method with Syntax : Class.method(instance)