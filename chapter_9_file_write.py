# str = "Hey vansh , you are amazing"

# f = open("myfile.txt", "w")

# f.write(str)

# f.close()

f = open("file.txt") #  default mode is read mode
lines = f.readlines() # return the content(all lines) in a list
print(lines, type(lines))

print(f.tell())
f.seek(0)
print(f.tell())

line1 = f.readline() #return each line one by one in a list
print(line1, type(line1))
line2 = f.readline() #return each line one by one in a list
print(line2, type(line2))
line3 = f.readline() #return each line one by one in a list
print(line3, type(line3))
line4 = f.readline() #return each line one by one in a list
print(line4, type(line4))
line5 = f.readline() #nothing aavailable after 4 lines
print(line5, type(line5))#nothing will be printed...
print(line5 == "") # will return True if line 5 is empty
print(f.tell())
f.seek(0)
print(f.tell())

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()