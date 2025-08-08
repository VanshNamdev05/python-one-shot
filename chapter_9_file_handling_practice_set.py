# f = open("poem.txt")

# content = f.read()
# if("twinkle" in content.lower()):
#     print("The word twinkle presnt in content")

# else:
#     print("The word twinkle not presnt in content")
    
# f.close()

import random

def game():
    print("You are playing the game")
    score =  random.randint(1,62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"Your scrore : {score}")
    if(score>hiscore):
        #write this hi score to the file
        with open("hiscore.txt" , "w") as f :
            f.write(str(score))            
    return score
game()