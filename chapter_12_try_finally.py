def main():
    try:
        a = int(input("Hey, Enter a number : "))
        print(a)
        return
        
    except Exception as e:
        print("Please Enter a Valid Number")   
        print(e)  
        return 
        
    finally:
        print("I am inside finally") 
        
main()

print("Thank You")