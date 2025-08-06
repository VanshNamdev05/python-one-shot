# num = int(input("Enter the number to get the multiplication table for : "))
# for i in range(1,11):
#     print(f"{num}*{i} = ",num*i)



# l = ["Vansh","Vanshika","Shubham"]
# for name in l:
#     if(name.startswith("V")):
#         print(f"Hello {name}")



# n = int(input("Enter a number : "))
# for i in range (2,n):
#     if(n%i==0):
#         print("Number is not prime")
#         break;
# else:
#     print("Number is prime")

'''
  *
 ***
*****
'''

# n = int(input("Enter the number : "))

# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")

'''
***
* *
***
'''

# n = int(input("Enter the number : "))
# for i in range (1,n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print("")    

num = int(input("Enter the number to get the multiplication table for : "))
for i in range(1,11):
    print(f"{num}*{11-i} = ",num*(11-i))