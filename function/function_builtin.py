"""
map,filter ,reduce
"""
#map

numbers1 = [1,2,3]
numbers2 = [4,5,6]

result = map(lambda x,y:x*y,numbers1,numbers2)
print(list(result))


#filter

numbers = [-3,-6,-5,2,5,6,-2]
less_than_zero = list(filter(lambda x:x<0,numbers))
print(less_than_zero)



#reduce
product = 1
list1 =[1,3,4,6]
for num in list1:
    product=product*num
print(product)
#LIST



import functools
product = functools.reduce((lambda x, y: x * y), list1)
print(product)


num = int(input("enter the number:"))
sum = functools.reduce((lambda x,y:x+y),range(num+1))
print(sum)