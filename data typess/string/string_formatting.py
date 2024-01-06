"""
python f-string
---------------

pyhton f-string is a newest python syntaxto do sting formatting.
It is available since Python 3.6
Oython f-string provide a faster ,more readeble,more concise,and less error prone way of formatting string in python.

The f-strings have the prefix and use {} brackets to evaluate values.
"""
name ='peter'
age = 23
#print('%s is %d years old'%(name,age))
#print('{} is {} years old'.format(name,age))
print(f'{name} is {age} years old')


bags =3
apples_in_bag=12
print(f'There are total of {bags * apples_in_bag} apples')