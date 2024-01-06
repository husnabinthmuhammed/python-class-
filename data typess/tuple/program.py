"""
1 write a python program to check whether  an element exist within a tuple
tuple1 =("apple",[10,20,30],(5,12,25),1,5,6,7)
"""
tuple1 =("apple",[10,20,30],(5,12,25),1,5,6,7)
print("apple" in tuple1)

"""
2.to convert a tuple into  a string
tuple2= ("s","t","r","i","n","g")
"""
tuple2= ("s","t","r","i","n","g")
print(''.join(tuple2))

"""
3.count the no of occurance of item 50 from a tuple 
tuple1 = (20,50,70,50,60,50)
"""
tuple1 = (20,50,70,50,60,50)
x = tuple1.count(50)
print(x)
