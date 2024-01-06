"""
My_list =[1,2,3,4,5]

"""
#1 sum of list items
My_list =[1,2,3,4,5]
sum=0
for i in My_list:
    sum = sum+i
print(sum)


#2 product of list items
My_list =[1,2,3,4,5]
pr=1
for i in My_list:
    pr *=i
print(pr)


""""
3.write a python program to convert a list of characters into a string
s = ['p','y','t','h','o','n']

"""
s = ['p','y','t','h','o','n']
str1 = ""
for i in s:
    str1 +=i
    print(str1)

#CONDITION AND STATEMENTS
a =33
b = 200
if b<a:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a is less than b")


"""
4.write a program to seperate negative and positive numbers from a given list?(accept input from the user)

"""
numbers =[1,5,6,-5,-2,-1,-7,0]
x = []
y = []
z = []
for i in numbers:
    if i>0:
        x.append(i)
    elif i ==0:
        z.append(i)
        print(z)
    else:
        y.append(i)
print("negative numbers",y)
print("positive numbers",x)


"""
5. program to find largest number in a given list with out using max ()

"""
mylist = [5,9,8.7,3,2]
#print(max(mylist))
#mylist.sort(reverse=True)
#print(mylist[-1])
max = mylist[0]
for i in  mylist:
    if max<=i:
        max=i
print(max)

"""
6.write a python program to find the common numbers from two lists

"""
list1 = [1,6,8,7,5]
list2 = [1,8,6,4,3,1]
new_list =[]
for i in list1:
    for j in list2:
        if i == j and i not in new_list:   #not in key word  used for second list iteration ie.,1 print only once
            new_list.append(i)

print(new_list)


"""
6.write a program to print even numbers from the list
"""

list1 = [1,6,7,8,4,3,9,2,10]
even =[]
odd =[]
for i in list1:
    if i%2==0 :
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

"""
7.write a python program to remove repeated elements from a given list without using built_in methods 
list_to_remove=["let's","google","the","pineapple","photo","google","photo",""]
"""
list_to_remove=["let's","google","the","pineapple","photo","google","photo",""]
new_list =[]
for i in list_to_remove:
        if i not in new_list :   #not in key word  used for second list iteration ie.,1 print only once
            new_list.append(i)
print(new_list)

"""
8.["www.zframez.com","www.wikipedia.org","www.asp.net","www.abcd.in"]
write a python program to print website suffixes(com,org,net,in)from this list.
"""
links = ["www.zframez.com","www.wikipedia.org","www.asp.net","www.abcd.in"]
for i in links:
    print(i)
    suffix = i.split('.')[-1]
    print(suffix)