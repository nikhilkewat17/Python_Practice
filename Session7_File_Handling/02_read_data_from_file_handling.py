# Read Existing file.
# Used "r" mode .

file=open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice.txt",'r')
read = file.read()
read2 = file.readline()  # read single line from file.
read3= file.readlines() # read all lines from file.

print(read)
file.close()

# OR
try:
    with open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice.txt",'r') as file:
        read = file.read()
        read2 = file.readline()  # read single line from file.
        read3 = file.readlines()  # read all lines in list from file.
        print(read)
except:
    print("File is not in reading Mode ...!")