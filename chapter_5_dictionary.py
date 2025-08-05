marks = {
    "Harry" : 100,    
    "Larry" : 50,    
    "Jerry" : 10,    
    10 : 9,
}

print(marks, type(marks))

print(marks["Harry"])

# DICTIONARY METHODS

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99,"Vanshika":100}) # vanshika willl be added in the dictionary
print(marks["Harry"])
print(marks)
print(marks.get("vansh"))
print(marks.get("vanshika"))
print(marks.get("Vanshika"))

# difference between marks.get() and marks[]
# marks[] gives error if not found... whereas marks.get() gives none

print(marks.get("Harry"))
# print(marks["Harry2"]) 

print(marks.pop("Larry"))
print(marks)

print(marks.popitem()) # will remove the last inserted element from the dictionary...
print(marks)

d = {} # this is empty dictionary
print(type(d))
    
print(len(marks))