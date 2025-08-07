# a = 12
# b = 45
# c = 56

# avg = (a+b+c)/3
# print(avg)

# def avg():
#     a=int(input("Enter the value of a : "))
#     b=int(input("Enter the value of b : "))
#     c=int(input("Enter the value of c : "))

#     average = (a+b+c)/3
#     print(average)

# avg()

# def printName(name , ending):
#     print(f"Hello, {name} {ending}")

# printName("Vansh","Thank You")
# b = printName("Namdev","Bye 😃")
# print(b)

# def returning(name):
#     return name

# c = returning("VANSH NAMDEV")
# print(c)

#DEFAULT PARAMETER

def greet(name="Guest"):
    print(f"Good Morning, {name}")
    
greet("Vansh")
greet()