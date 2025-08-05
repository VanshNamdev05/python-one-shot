s = {} # this is empty dictionary
print(type(s))

ss = set() # this is empty set
print(type(ss))

set1 = {1,2,3,1,2,3,1,2,3,1,2,3} # elements in the set doesn't repeat
print(set1, type(set1))

set2 = {1,2,3,4,5,6,7,8,9}
print(set2)

set3 = {1,2,"vansh","haha",88}
print(set3)

# SETS METHODS

set3.add(566)
print(set3, type(set3))

print(len(set3))

set3.remove(1)
print(set3)

set3.pop() # will remove random item from sets
print(set3)

# UNION

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

s3 = s1.union(s2) # all unique values in s1 and s2
print(s3)

s4 = s1.intersection(s2) # common values in s1 and s2
print(s4)
