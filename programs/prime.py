"""
1.to check whether a number is prime or not

"""

num=int(input("enter the number:"))
flag=False
for i in range (2,num):
    if num % i ==0:
        flag=True
        break
if flag ==True:
    print(num,"not prime")
else:
    print(num,"the num is prime")
    
    
    















