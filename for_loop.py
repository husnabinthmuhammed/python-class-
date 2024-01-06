"""
print n natural numbers
"""
#n=int(input("enter the range:"))
#for i in range (n+1):
#    print(i)

"""
Write a python program that prints all the numbers from 0 to 6 exept 3 and 6
"""
#n = 6
#for i in range (0,n):
#    if(i==6 or i==3 ):
#        continue
#    print(i)

"""
write a python program  to get the fibonacci series between 0 to 50
"""
#num = 50
#n1 = 0
#n2 = 1
#for i in range(num+1 ):
#    print(n1)
#    n3 = n1+n2
#    n1=n2
#    n2=n3


"""
write a python  program to print multiplication table of a given number
"""
#n = int(input("Enter the  number:"))
#for i in range(1,11):
#    mul=i*n
#    print(i,"*",n,"=",mul)

"""

______to find factorial of a number_____


n = int(input("enter the number:"))
fact =1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
print("factorial of",n,"is",fact)

"""



"""
______print divisible by 3 in range from 1 to 50_____


n = 50
for i in range (1,51):
    if(i%3==0):
        print(i)

"""
"""
fruits = ['apple','orange','banana','kiwi','grapes']
newlist =[]
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)

fruits = ['apple','orange','banana','kiwi','grapes']
newlist =[x for x in fruits if "a" in x]
print(newlist)
"""



"""
____________print odd or even________________
list_items = [1,8,3,4,5,6,7]
even = [i for i in list_items if i%2==0]
print(even)
odd = [i for i in list_items if i%2!=0]
print(odd) 

"""