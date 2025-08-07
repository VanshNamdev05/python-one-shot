# It is a function which calls itself
'''
fact(n) = n * fact(n-1)
where, fact(n-1) = (n-1) * (n-2) * ...* 3 * 2 * 1 
'''

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

a = fact(3)
print(a)