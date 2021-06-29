#!/usr/bin/python3

num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
operator = input("enter the operation you want to perform: ")

if(operator == 'add'):
    result = float(num1) + float(num2)
    print(result)
elif(operator == 'sub'):
    result = float(num1) - float(num2)
    print(result)
elif(operator == 'mul'):
    result = float(num1) * float(num2)
    print(result)
elif(operator == 'div'):
    result = float(num1) / float(num2)
    print(result)
else:
    print("please enter the valid operation")
    
    
