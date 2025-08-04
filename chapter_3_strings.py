name = "Vansh";
#string is immutable...
# string slicing...

print(len(name))
shortName = name[0:3] # excluding 3...
print(shortName)

shortName1 = name[-5:-2] # negative indexing...
print(shortName1)

print(name[:])
print(name[0:])
print(name[:4])
print(name[::2]) # print by skipping next value ... i.e ---> print second word skipping the first word after

# String functions...

print(len(name))
print(name.startswith("Van"))
print(name.startswith("Vaa"))
print(name.endswith("sh"))
print(name.endswith("Sh")) # case sensitive
print(name.endswith("nash"))

name2 = "vansh namdev"
print(name2.capitalize())
print(name2.upper())
print(name2.lower())

print(name2.find("a"))

aa = name2.replace("vansh","Vanshika")
print(aa)

# Escape sequence characters

a = "Vansh is a good boy\nbut not a bad boy"
print(a)

b = "Vansh\tNamdev"
print(b)

c = 'Vansh\'s favourite sabji is paneer'
print(c)