class Employee:
    def __init__(self ,name , email):
        self.name = name
        self.email = email

    def display_info(self):
        print("%s is employee of this organisation and his email id is %s ...!" %(self.name,self.email))
# emp=Employee("Nikhil","nikhilkewat17@gmail.com")
# emp.display_info()

class Developer(Employee):
    def __init__(self,name,email,program_lang):
        super().__init__(name,email)
        self.program_lang = program_lang
    def display_info(self):
        print("%s is '%s developer' of this project and his email id is '%s' ...!" %(self.name ,self.program_lang,self.email))
developer1= Developer("Nikhil Kewat" , "nikhilkewat17@gmail.com" ,"Python")
developer2= Developer("Kiran Sarode","kiran12@gmail.com","React-Js")
# developer1.display_info()
# developer2.display_info()

class Manager(Employee):
    def __init__(self,name ,email,emp_list = None):
        super().__init__(name,email)
        if emp_list is None:
            self.emp_list = []
        else:
            self.emp_list = emp_list
    def add_emp(self,emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)
    def remove_emp(self,emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)
    def display_employee_list(self):
        print(f"{self.name} team is :")
        for emp in self.emp_list:
            emp.display_info()
manager1  = Manager("Sandip Patil","sandippatil1234@gmail.com",[developer1,developer2])
manager1.display_employee_list()  # Print Sandip sir team employees


manager1.remove_emp(developer2) # Remove one employees from team
manager1.display_employee_list() # Return sandip sir team