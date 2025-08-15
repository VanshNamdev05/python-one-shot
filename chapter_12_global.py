a = 89 # global variable which can be used everywhere
def func() : 
    # a = 3 # Local variable of func function
    global a
    a = 3 # will change the original global a variable
    print(a)
    
func()
print(a)