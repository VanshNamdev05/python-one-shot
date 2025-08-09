class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")

    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")

    c=3

# o = Employee()
# print(o.a)
# print(o.b) # shows an error as there is no b attribute in Employee class

# i = Programmer()
# print(i.a)
# print(i.b)
# print(i.c) # error(same reason as above)

u = Manager()
print(u.a, u.b, u.c)