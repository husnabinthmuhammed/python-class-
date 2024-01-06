"""
try to create hollow diamond pattern
"""
#n = int(input("Enter the number of rows:"))
# Upper part of hollow diamond
#for i in range(1, n+1):
#    for j in range(1,n-i+1):
#        print(" ", end="")
#    for j in range(1, 2*i):
#        if j==1 or j==2*i-1:
#            print("*", end="")
#        else:
#            print(" ", end="")
#    print()

# Lower part of hollow diamond
#for i in range(n-1,0, -1):
#    for j in range(1,n-i+1):
#        print(" ", end="")
#    for j in range(1, 2*i):
#        if j==1 or j==2*i-1:
#            print("*", end="")
#        else:
#            print(" ", end="")
#    print()

"""
create heart shape pattern 
"""
#num=int(input("Enter the number:"))
#n=num//2
#for i in range(n):
#    for j in range(n-i):
#        print(" ",end="")
#    for k in range(i):
#        print("* ",end="")
#    for j in range(2*(n-i)):
#        print(" ",end="")
#    for k in range(i):
#        print("* ",end="")

#    print()

#for i in range(1,num+1):
#    for j in range(i):
#        print(" ",end="")
#    for k in range(num-i):
#        print("* ",end="")
#    print()


"""
half pyramid pattern with number
"""
#n=int(input("Enter the number of rows:"))
#for i in range(n):
#    for j in range(i + 1):
#        print(j + 1, end=" ")
#    print("\n")

"""
reverse pattern from 10 to 1

"""
#n = int (input("Enter teh number:"))
#for i in range (0,n+1):
#    for j in range(n-i,0,-1):
#        print(j,end="  ")
#    print("\n")

"""
equilatrial triangle pattern with charecters 
"""
"""
for i in range (65,91):#97-123(lowercase)
    print(chr(i),end=' \n')
    
import string
for i in string.ascii_lowercase:
    print(i.end=" ")
"""

#n = int(input("enter the level you want:"))
#k1 = 1
#for i in range(n+1):
#    for j in range(n - i):
#        print(' ',end=' ')
#    for k in range(i):
#        ch = chr(64+k1)
#        print(ch,end='   ')
#        k1+=1
#    print()


"""
print H 
"""
n = 7
for i in range (1,n+1):
    for j in range(1, 2*n):
        if j==1 or j==2*n-1 :
            print("*", end=" ")
        else:
            print(" ", end="")
    print()




