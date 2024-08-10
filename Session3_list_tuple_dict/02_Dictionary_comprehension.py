dict = { "id":1 , "Name" : "Nikhil Kewat" , "Age":26 }

print(dict)

print(dict["Name"])
print(dict["Age"])

print(dict.keys())
print(dict.values())

print(dict.get("Name"))

print(dict.items())

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

# item method
for i in dict.items():
    print(i)

# Update method
dict.update({"salary":90000 , "City":"Aurangabad"})
print(dict)

# Pop method
dict.pop("salary")
print(dict)

# copy method
new = dict.copy()
print("New Dictionary is : " , new)

# clear method
new.clear()
print(new)
dict1 = {"Nikhil":500000, "Kiran":5000 , "Akash":45000}

dict_comprehension = { key:dict1[key]+10000 for key in dict1 }
print(dict_comprehension)

# In method
word = "Nikhil_Govind_Kewat"
word_counter = {}
for i in word:
    if i in word_counter:
        word_counter[i] += 1
    else:
        word_counter[i] = 1

print(word_counter)


