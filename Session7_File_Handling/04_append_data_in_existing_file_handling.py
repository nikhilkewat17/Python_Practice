# Append data into existing file.

# using mode "a"

file = open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice.txt" , "a")
file.write("Good Morning universe , thank you much for today and make my day happy")
file.close()


# OR :

try:
    with open(r"C:\Users\Hp\PycharmProjects\nikcoder\Session7_File_Handling\data\practice.txt","a") as file :
        file.write("Thank You so much universe your trying to make me data engineer")
        print("Data is append Succesfully...!")
except Exception as e:
    print("Data is not append please check error : " , e)

