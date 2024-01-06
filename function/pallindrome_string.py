"""__________PALLINDROME STRING OR NOT________"""

def reverse(string):
    string = [string[i]for i in range (len(string)-1,-1,-1)]
    print(string)
    print(s)
    x = "".join(string)
    if x==s:
        print("pallindrome")
    else:
        print("not pallindrome")
    return x
s = input("enter the string:")
print(reverse(s))









s=input("enter a string:")
x=s[::-1]
if s==x:
    print("pallindrome")
else:
    print("not pallindrome")