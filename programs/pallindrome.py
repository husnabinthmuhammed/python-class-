"""
write a program to print the pallindrome
"""
number = int(input("enter e number:"))
rev=0
temp = number
while number>0:
    rem = number%10
    rev =(rev*10)+rem
    number=number//10
if temp==rev:
    print("pallindrome")
else:
    print("not palindrome")



