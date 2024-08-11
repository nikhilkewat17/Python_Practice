# writing in Existing file.
# Used "w" mode .

file=open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice2.txt",'w')
write_string = file.write("Welcome to nikcoder data engineering...!")

write_lines = file.writelines("Nikhil Kewat, Kiran sarode,Akash Gadge ") #write list string

file.close()

# OR
try:
    with open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice2.txt",'w') as file:
        file.write("Welcome to nikcoder data engineering...!")
        print("Data is writing succesfully..!")
except:
    print("File is not in writing Mode ...!")