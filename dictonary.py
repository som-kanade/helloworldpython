#!/usrbin/python3

student = {'Name': 'Mike', 'age': 25, 'courses': [1,2,3]}

d1 = {}

try:
    del student['phone']
except:
    print("didnot find key")
