friends = ["apple","orange",5,345.93,False,"Rohan"]
print(friends)

print(friends[0])

for friend in friends:
    print(friend)
    
friends[0] = "VANSH" # unlike strings... lists are mutable

print(friends)

print(friends[1][1])

friends.append("HARRY")
print(friends)

l1 = [1,66,2,3,66,4,5,2,3,1,99,0,32,687]
l1.sort()
print(l1)

# l1.reverse()
# print(l1)

l1.insert(3,3333333333) #insert 3333333333 at index 3 in l1
print(l1)

print(l1.pop()) # will remove the last element and print the removed element

print(l1.pop(2)) # will remove the second index element and print that element
print(l1)

l1.remove(1)
print(l1)

# l1.remove(1) # ---> will give error as there is no 1 present in the string now...
# print(l1)

