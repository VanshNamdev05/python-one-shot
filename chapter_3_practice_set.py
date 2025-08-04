name = input("Enter your name : ")
print(f"Good afternoon {name}") # f string

print("Good afternoon " + name)
print("Good afternoon ",name)

a = """Dear NAME ,
You are selected!
DATE"""

print(a.replace("NAME","Vansh").replace("DATE","4 august 2025"))