class Employee:
    language = "py"
    salary = 1200000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
      
    @staticmethod  
    def greet():
        print("Good morning")
    
harry = Employee()
harry.language = "JS"
harry.getInfo() # ---> will be automatically converted to Employee.getInfo(harry)
Employee.getInfo(harry)
# above 2 line will provide the same output
harry.greet()