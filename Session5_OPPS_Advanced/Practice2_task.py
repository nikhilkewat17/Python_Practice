class Student:
    def __init__(self,rno,name,email,marks,cno=0):
        self.rno = rno
        self.name = name
        self.email= email
        self.marks = int(marks)
        self.__cno = int(cno)

    def __get_grade(self,marks):
        self.marks = marks
        if self.marks > 90 and self.marks <= 100:
            return"A grade"
        elif self.marks >= 70 and self.marks <=90:
            return "B Grade"
        elif self.marks >= 50 and self.marks <= 70 :
            return "C grade"
        else:
            return "D Grade"
    def display_details(self):
        print(f"Roll No {self.rno} is {self.name} and email {self.email} contact number {self.__cno} obtained '{self.__get_grade(marks=self.marks)}' " )
        # return self.__get_grade(marks=self.marks)

stu1 = Student(12,"Nikhil Kewat","nikhil@gmail.com",98,721871656)
stu1.display_details()
