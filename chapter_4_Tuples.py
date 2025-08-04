a = (1,2,3,4,5,6,7)
print(type(a))

# Tupple is immutable...

b = ()
print(type(b))

c = (1) # it will be treated as a number (int)
print(type(c))

d = (1,) # Tuple with only one element
print(type(d))

tup1 = (1,1,32,22.44,False,"VANSH")
# tup[0] = 112233 # cannot change as tuple is immutable

print("=======================TUPLE METHODS===========================")

print(tup1.count(1))

print(tup1.count(111111))

print(tup1.index(1))

print(1 in tup1)

repeated = tup1*2
print(repeated)

print(len(tup1))
print(len(repeated))

# min and max only works if all the elements are integer
tup2 = (1,2,3)
print(min(tup2))
print(max(tup2))

a,b,c = tup2
print(a,b,c)