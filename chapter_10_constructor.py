class Employee:
    language = "py"
    salary = 1200000
    
    def __init__(self, name, salary, language): # will be automatically called (dunder method)
        print("I am creating an object") 
        self.name = name
        self.salary = salary        
        self.language = language
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
      
    @staticmethod  
    def greet():
        print("Good morning")
    
harry = Employee("HARRY","1300000","JAVASCRIPT")
harry.name = "Harry"
print(harry.name, harry.salary, harry.language)