a = 1 # a is an integer
print(type(a))

b = 2 # b is an integer
print(type(b))

print(a+b)

# python automatically detects the type of the variables...

c = 1.72 # c is a floating point number
print(type(c))

d = False # d is a boolean variable
print(type(d))

e = None # e is a none type variable
print(type(e))

f = "Vansh"
print(type(f))

_sameer = 34

# @sameer = 34 ---> invalid syntax

# s@meer = 34 ---> invalid syntax
g = 99
print(g)
print(type(g))
g = "99"
print(g)
print(type(g))

h = "31.2"
print(h)
print(type(h))
i = float(h)
print(i)
print(type(i))

aa = input("Enter number 1 : ")
bb = input("Enter number 2 : ")

print("Number a is : ",aa)
print("Number b is : ",bb)
print("Sum is : ",aa+bb) # it will take input as string and the result will be 12...
print("Vansh"+"Coder")

# To solve this problem use the following syntax : 

aaa = int(input("Enter the first number : "))
bbb = int(input("Enter the second number : "))
print(aaa+bbb)