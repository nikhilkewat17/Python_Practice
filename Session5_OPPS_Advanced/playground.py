class Cycle:
    num_wheels = 2
    num_bycles_created = 0
    def __init__(self,brand ,model):
        self.brand = brand
        self.model = model

    def info(self):
        print("Welcome to our '%s' family you choose '%s' and %d tyre bike ...!"%(self.brand,self.model,self.num_wheels))

bike1 = Cycle("Honda","Shine")
bike1.info()

bike2 = Cycle("Hero","Splendor")
bike2.info()
#print(bike2.num_wheels)


bike3 = Cycle("Yamaha","FZ")
bike3.info()

# using class and and change class variable values
Cycle.num_wheels = 5
Cycle.num_bycles_created = 40
print("The number of wheels of your bike is %d and company make %d bikes in warehouse" %(Cycle.num_wheels ,Cycle.num_bycles_created))

# using instance(object) of class and change class variable value for that instance
bike3.num_wheels = 4
bike3.num_bycles_created = 45
print("The number of wheels of %s bike is %d and company make %d bikes in warehouse" %(bike3.model,bike3.num_wheels ,bike3.num_bycles_created))
