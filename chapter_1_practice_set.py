# print("""This can be used to :
#       write multiple lines at once
#       without using single quote to print single line""")

# for i in range (1,11):
#     print(5*i)

# import pyttsx3
# engine = pyttsx3.init()

# engine.say("""I don't wanna die or fade away
#             I just wanna be someone
#             I just wanna be someone""")

# engine.runAndWait()

import os

directory_path = '/'

contents = os.listdir(directory_path)

# print(contents)

for item in contents:
    print(item)