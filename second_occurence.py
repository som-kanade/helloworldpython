#!/usr/bin/python3

l1 = ["aa", 'bb', 'cb', 'aa', 'ed', 'word', '6b', 'aa', 'bb']
occurence = {}

for i in l1:
    if i not in occurence:
        occurence[i] = 1 
    else:
        occurence[i] +=1 
        
print(occurence)
# list1 = (list(occurence))
# print(list1)
# print(list1[1])


