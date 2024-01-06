"""
Exception handling
_____________________

1.try
2.except
3.finally

"""

try:
    num = int(input("Eneter the number:"))
    result = num/0
except:
    print("you can't divide by zero")

#-------------------------------------------------------------

try:
    file = open("new_methods.py",'r')
    print(file.read())
except:
    print("file does not exist ")
