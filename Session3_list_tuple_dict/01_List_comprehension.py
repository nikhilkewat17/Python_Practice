list = [1,2,3,4,5,6,7,8,9,10]
new = []

#Single if condition
for i in list:
    if i%2 == 0:
        new.append(i)
new = [ x for x in list if x%2 == 0] # List Comprehension single if condition
print(new)

#double condition if and else
for i in list:
    if i%2==0:
        new.append("Even")
    else:
        new.append("Odd")
print(new)
new = ["Even" if x%2==0 else "Odd" for x in list]  # List comprehension if else condition
print(new)


# Using Range function .
list = []
for i in range(21):
    if i%2==0:
        list.append("Even")
    else:
        list.append("Odd")
print(list)
list = ["Even" if x%2==0 else "odd" for x in range(21)]
print(list)