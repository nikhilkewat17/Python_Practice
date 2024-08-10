class Student:
    def __init__(self,rno,first_name,last_name,marks):
        self.rno = rno
        self.first_name = first_name
        self.last_name = last_name
        self.marks = marks
    print("\n")
    @property
    def display_info(self):
        return f"Hello {self.first_name} {self.last_name} your roll no is {self.rno} and your obtained {self.marks} marks ...! \n"

    @property
    def email(self):
        return "%s your email id is %s%s%d@gmail.com \n" %(self.first_name,self.first_name.lower(),self.last_name.lower(),self.rno)

    @property
    def fullname(self):
        return "Roll no %d is %s %s ...! \n" %(self.rno,self.first_name,self.last_name)

    @fullname.setter
    def fullname(self, name):
        """Allow setting full name, which updates first and last names."""
        first, last = name.split()
        self.first_name = first
        self.last_name = last
    #
    #
    # Deleter for the full name

    @fullname.deleter
    def fullname(self):
        """Delete the full name and reset first and last names to None."""
        print("Deleting Name!")
        self.first_name = None
        self.last_name = None

stu1=Student(17,"Nikhil","Kewat",89)
print(stu1.display_info)
print(stu1.fullname)
print(stu1.email)

print("Change fullname and get automatically change email id :-----------\n")
stu1.fullname = "Kewat Nikhil"
print(stu1.fullname)
print(stu1.email)

del stu1.fullname
print(stu1.fullname)