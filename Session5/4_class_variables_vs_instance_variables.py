class Bicycle:
    # Class variables
    num_wheels = 2  # All bicycles typically have 2 wheels
    num_bicycles_created = 0  # Counter for the number of Bicycle instances created

    def __init__(self, make, model):
        # Instance variables
        self.make = make
        self.model = model
        # Increment the class variable using the class name
        Bicycle.num_bicycles_created += 1

    def display_info(self):
        # Accessing class variable using self
        print(f"Make : {self.make} ,Model : {self.model} has {self.num_wheels} wheels.")

# Create instances of Bicycle
bike1 = Bicycle("Trek", "Emonda")
bike2 = Bicycle("Giant", "Defy Advanced")

# Class variables can accessed directly using class and its instances .
print(Bicycle.num_wheels)
# print(Bicycle.make)

# However, instance variables can be accessed using respective instance only
print(bike1.make)
print(bike1.num_wheels )

# accessing class variable by using class and instances
print(Bicycle.num_bicycles_created)
print(bike1.num_bicycles_created)
print(bike2.num_bicycles_created)

# update value for single instance
bike2.num_wheels = 3
print(Bicycle.num_wheels)
print(bike1.num_wheels)
print(bike2.num_wheels)

# Update class variable value
Bicycle.num_wheels = 3
print(Bicycle.num_wheels)
print(bike1.num_wheels)
print(bike2.num_wheels)

# Display total bicycles created using a class method
print(f"Total bicycles created: {Bicycle.num_bicycles_created}")