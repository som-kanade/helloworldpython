#!/usr/bin/python3
from collections import Counter

a = "aaaabbbaabcccdd"
my_couter = Counter(a)
print(type(my_couter.most_common(2)[1]))

print(my_couter.most_common(2)[1][0])
