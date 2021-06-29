#!/usr/bin/python3 

f = open("employee.txt", "r")

for line in f.readlines():
    print(line)
