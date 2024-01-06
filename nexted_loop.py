"""
print the pattern
"""
n=int(input("Enter the number of rows:"))
for i in range (1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range (i):
        print('* ',end='')
    print()
"""
reverse the pattern
"""
#n=int(input("Enter the number of rows:"))
#for i in range (n+1):
#   for j in range(i):
#        print(' ',end='')
#   for k in range (n-i):
#        print('* ',end='')
#   print()
"""
print numbers pattern
"""
#n=int(input("Enter the number of rows:"))
#for i in range (1,n+1):
#    for j in range (n-i):
#       print(" ",end='')
#    for k in range (i):
#        print(k ,end=" ")
#    print()

"""
print diamond pattern
"""
#n= int(input("enter the diamond length:"))
#for i in range (1,n+1):
 #       for j in range (n-i):
 #            print(" ",end='')
 #       for k in range (i):
  #          print("* ",end="")
 #       print()
#for i in range (1,n+1):
#   for j in range(i):
#        print(' ',end='')
#   for k in range (n-i):
#        print('* ',end='')
#   print()

"""
reverse of diamond
"""

n=int(input("Enter the number of rows:"))
for i in range (n-1):
   for j in range(i):
        print(' ',end='')
   for k in range (n-i):
        print('* ',end='')
   print()
for i in range (1,n+1):
    for j in range (n-i):
       print(" ",end='')
    for k in range (i):
        print("*" ,end=" ")
    print()



