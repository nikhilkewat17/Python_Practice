# 1 Read File data

file = open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice.txt" , "r")

print(file.read())

# print(file.readline())   # This readline Funtion show single line of data .

# print(file.readlines()) # This readlines Funtion show all lines of data .


# 2 Write data in file

file2 = open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice_self.txt" , "w")

text = input("Enter data to write in file : ")
file2.write(text + "\n")

file2 = open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice_self.txt" , "r")
print(file2.read())


# 3 Append data in file

file4 = open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice_self.txt" , "a")
text = input("Enter data to append  in file : ")
file4.write(text + "\n")

file4 = open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice_self.txt" , "r")
print(file4.read())

# 4 Delete File

file5 = open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice_self.txt" , "w")
print(file5.write(""))

file5 =open(r"C:\Users\Hp\OneDrive\Desktop\FileHandling\Practice_self.txt" , "r")
print(file5.read())


