# Creating file if file is not exists or present.

file=open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice.txt",'x')
print("File created succesfully...!")
file.close()


# OR

try:
    with open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice.txt",'x') as file:
        file.write("Hello Nikhil")
except:
    print("File already Present")


