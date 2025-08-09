import random
a = random.randint(1,100)
print(a)

score = 0
n = -1

while(n!=a):
    
    n = int(input("Enter your guess : "))

    if(n>a):
        print(f"{n} is greater. Guess Lower !")

    else:
        print(f"{n} is lower. Guess Higher !!!")
        
    score = score+1
    
print(f"Your guess {n} is equal to the number {a}")
print(f"Your score is {100-score}")