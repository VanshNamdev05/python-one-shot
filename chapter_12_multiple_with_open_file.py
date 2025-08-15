with(
    open("file.txt") as f1,
    open("myfile.txt") as f2,
) : 
    a = f1.read()
    b = f2.read()
    
print(a)
print(b)