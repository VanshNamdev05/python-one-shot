try:
    a = int(input("Hey, Enter a number : "))
    print(a)
    
except Exception as e:
    print("Please Enter a Valid Number")   
    print(e)   
    
else:
    print("I am inside else") 

print("Thank You")