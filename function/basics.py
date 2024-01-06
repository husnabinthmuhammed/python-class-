"""
function
______________
A function is a block of code which only runs when it called ,
A function can return a data as a result.

return____
sum(a+b)
retun sum


:parameter
which is defined in part of function call

:argument
which is defined in the part of fn defnition
"""


"""
def sum():
    a = 6
    b = 7
    c = a+b
    print(c)
sum()


def sum(a,b):
    return a+b
print(sum(6,7))
"""

#sum of n  natural numbers
"""
def sumofNnums(num):
    s = 0
    for i in range (num+1):
        s = s+i
    return s
num = int(input("enter the range of nums:"))
print(sumofNnums(num))
"""
#find the greatest of 3 number
"""
def max():
    if (a >= b) and (a >= c):
        return a
    elif (b >= c) and (b >= a):
        return b
    else:
        return c


a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
print(max())
"""
#find the sum of list of numbers
numbers = [1,2,3,4,5,6,7,8]

def sumlist(numbers):
    s = 0
    for i in numbers:
        s = s+i
    return s
print(sumlist(numbers))
