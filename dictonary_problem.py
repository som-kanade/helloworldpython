#!/usr/bin/python3

phoneBook = {}
for i in range(int(input("enter count: "))):
    key = input("enter key: ").strip()
    val = int(input("enter value: "))
    phoneBook[key] = val
    
