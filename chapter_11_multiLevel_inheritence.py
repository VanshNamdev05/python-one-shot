class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

o = Employee()
print(o.a)
# print(o.b) # shows an error as there is no b attribute in Employee class

i = Programmer()
print(i.a)
print(i.b)
# print(i.c) # error(same reason as above)

u = Manager()
print(u.a)
print(u.b)
print(u.c)