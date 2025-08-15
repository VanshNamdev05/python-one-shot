# l = [1,2,3,4,5]

# index = 0
# for item in l:
#     print(f"The item number at {index} is {item}")
#     index += 1




# This can be simplified using enumerate function

l = [1,2,3,4,5]
for index, item in enumerate(l):
    print(f"The item number at {index} is {item}")