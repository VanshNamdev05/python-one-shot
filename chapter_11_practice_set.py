# class TwoD:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
        
#     def show(self):
#         print(f"The vector is {self.i}i +{self.j}j")
        
# class ThreeD(TwoD):
#     def __init__(self, i, j, k):
#         super().__init__(i,j)
#         self.k = k
    
#     def show(self):
#         print(f"The vector is {self.i}i +{self.j}j + {self.k}k")
        
# a = TwoD(1,2)
# a.show()
# b = ThreeD(1,2,3)
# b.show()



# class Animal:
#     pass

# class Pet(Animal):
#     pass

# class Dog(Pet):
#     @staticmethod   
#     def bark():
#         print("Bow Bow !!!")
    
# d = Dog()
# d.bark()



# class Employee:
#     pass

# e = Employee()
# e.salary = 234 # Instant attribute
# e.increment = 20 # Instant attribute



# class Employee:
#     salary = 234
#     increment = 20
    
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + (self.salary * self.increment)/100)

# e = Employee()
# print(e.salaryAfterIncrement)





class Employee:
    salary = 234
    increment = 20
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * self.increment)/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100
        

e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)