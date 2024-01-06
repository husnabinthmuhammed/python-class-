"""
_______________________________________________________
1.Multiply all the numbers in a list using function
nums = [7,6,2,3,1]
-------------------------------------------------

nums = [7,6,2,3,1]

def mullist(nums):
    mul = 1
    for i in nums:
        mul = mul*i
    return mul
print(mullist(nums))

"""
"""
_________________________________________________________________________________________________________________________________
2.W A P function to calculate the factorial of a number (a non negative number ).The function accepts the numbers as an argument.
----------------------------------------------------------------------------------------------------------------------------------
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n = int(input("Enter the number:"))
print(factorial(n))
"""
"""
________________________________________________________________
3.generate a python list of all the even numbers between 4 to 30
________________________________________________________________
list1 =[]
def list(nums):
    for i in range(4,30):
        if i%2==0:
            list1.append(i)
    return list1
print(list(30))
_____________________________OR___________________________________
def even():
    even_num = [i for i in range(4,31)if i%2==0]
    return even_num
print(even())
"""

"""
___________________________________________________________________________________
WAP function that take a number as a parameter and check the number is prime or not
____________________________________________________________________________________

def prime():
    flag=False
    for i in range (2,num):
        if num % i ==0:
            flag=True
            break
    if num ==1:
        print(num,"not prime")
    else:
        print(num,"the num is prime")
num=int(input("enter the number:"))
prime()
"""