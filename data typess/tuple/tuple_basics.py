"""
immutable,ordered,indexed,allows duplicates
"""
thistuple =( "apple",89,6,"banana","apple",[678,'fghjk'])
print(thistuple)
tple ="orange",
print(type(tple))

print(thistuple[4])
print(thistuple[5][0])
print(thistuple[::-1])

x = list(thistuple)
#print(x.append('gsdftgf'))
x[0] ='grapes'
print(tuple(x))

thistuple =( "apple",89,6,"banana","apple",[678,'fghjk'])
tupl =("husna","aju","athu")
print( thistuple + tupl )

x = list(thistuple)
x.extend((tupl))
print(tuple(x))

#looping through string
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (index,letter)
    index = index +1


thistuple = ("apple","banana","cherry",[8,"rtyu",0])
index =0
for i in thistuple:
    print(index,i)
    index = index+1

#emumerate
thistuple = ("apple","banana","cherry",[8,"rtyu",0])
x = enumerate(thistuple)
print(list(x))


thistuple = ("apple","banana","cherry",[8,"rtyu",0])
print(thistuple[3][::-1])
print(thistuple[3][0])



