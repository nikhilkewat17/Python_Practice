print("String Module Programs : ")
from modules.string_ops import string_operations_module

string = "nikhil"

print(string_operations_module.capitalize_string(string))
print(string_operations_module.reverse_string(string))
print(string_operations_module.count_vowels(string),"\n")


# Math Module
print("Math Module Programs : ")
from modules import math_operations_module
x = int(input("Enter a number x : "))
y = int(input("Enter a number y : "))
print(math_operations_module.add(x,y))
print(math_operations_module.divide(x,y))
print(math_operations_module.multiply(x,y) ,"\n")



# List Module import and call here
print("List Module Programs : ")
from modules import list_operations_module

list = [ "Nikhil" , "Kewat" ]

list2 = [1,2,34,5,6]

print(list_operations_module.sort_list(list))
print(list_operations_module.find_max(list2))
print(list_operations_module.find_min(list2))
print(list_operations_module.average(list2))