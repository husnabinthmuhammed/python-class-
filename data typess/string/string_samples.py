""""
string-immutable data types , indexed,ordered,allows duplicate

"""
str1 = "Hello World"

#string indexing
print(str1[0])
print(str1[2])
print(str1[8])
print(str1[-1])
print(str1[8])

#string slicing
print(str1[3:8])
print(str1[0:5])
print(str1[6:11])
print(str1[::-1])
print(str1[::-2])
print(str1[::-3])
print(str1[:-6:-1])
print(str1[-7::-1])

#string methods
str1 = "Helloworld"
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print(str1.islower())
print(str1.isupper())
print(str1.find("hello"))

list1 = ["apple","banana","orange"]
x = ' '.join(list1)
print(x)

print(str1.__dir__())
print(str1.isalnum())
print(str1.isspace())
print(str1.split())


name = "husna binth muhammed"
print(name.split())


name = "Husna Binth Muhammed"
print(name[3])
print(name[::-1])
print(name[:20:])
print(name[:5])
print(name[::-3])
print(name[::2])



s1 = "Python"
s2 = "Luminar"

mid = int(len(s1)/2)
print(mid)
x=s1[:3]+s2+s1[3:]
print(x)


mids1 = int (len(s1)/2)
print(mids1)
mids2 = int(len(s2)/2)
print(mids2)
x = s1[0]+s2[0]+s1[mids1]+s2[mids2]+s1[-1]+s2[-1]
print(x)



#convert a string into a list
str1 = "hi dears"
x = (list(str1))
print(x)
print(type(x))
y = ''.join(x)
print(y)
print(type(y))