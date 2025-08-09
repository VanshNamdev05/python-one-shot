class Employee:
    language = "py"
    salary = 1200000
    
harry = Employee()
harry.name = "Harry" #Instance attributes
print(harry.name, harry.language, harry.salary)
rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.language, rohan.salary)

# Here name is Instance attribute and 
# salary and language are class attributes as they directly belong to the class...
