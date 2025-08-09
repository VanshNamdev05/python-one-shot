class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the company is : {self.company}")
class Coder():
    language = "PYTHON"
    def printLanguages(self):
        print(f"Out of all the languages , here is your language : {self.language}")

class Programmer(Employee, Coder):
    language = "JS"
    def showLanguage(self):
        print(f"He is good with {self.language} language")    
    

a = Employee()
b = Programmer()

print(a.company, b.company)
b.show()
b.printLanguages()
b.showLanguage()