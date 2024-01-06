"""
list
____
mutable(changable),indexed,ordered,allows duplicates


"""
list_items = ["apple","orange","mango","grapes"]
print(list_items)
print(list_items[0])
print(list_items[-1])
print(list_items[1:])
print(list_items[::-1])
print(list_items[:-1])
print(list_items[0][-2])
print(list_items[1:3])
list_items[1]='pineapple'
print(list_items)
print(list_items[0][2:])


#nested list
list_items = ["apple","orange","mango","grapes",["python","react","django"]]
print(list_items[4][0])
print(list_items[4][1:3])
print(list_items[4][::-1])
print(list_items[4][0][::-1])
list_items[4].insert(1,'golang')  #insert using any position  insertion
print(list_items)
list_items[4].append("angular")  #append used for last position insertion
print(list_items)

list2 =["vento","bmw","audi","ford"]
list_items.extend(list2)
print(list_items)

list_items[4].remove("python")
print(list_items)

list_items[4].pop(1)
print(list_items)

list_items[4].clear()
print(list_items)

list_items.reverse()
print(list_items)

list2.sort()
print(list2)

x = list2.count("b")
print(x)
