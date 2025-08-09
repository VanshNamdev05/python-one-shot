class Employee:
    language = "py"
    salary = 1200000
    
harry = Employee()

harry.language = "JS" #Instance attributes (takes preference over class attributes)

print(harry.language, harry.salary)
rohan = Employee()
rohan.name = "Rohan"
print(rohan.language, rohan.salary)

# Here name is Instance attribute and 
# salary and language are class attributes as they directly belong to the class...
# here harry's language will be changed to JS