"""
mutable,ordered,indexed,duplicates not allowed

"""
dict1 ={"name":"athu","age":1,"place":'abc',"course":"python"}
print(dict1)

##get a purticular value
print(dict1["age"])
print(dict1.get("name"))

#to change the value
dict1["name"]="aju"
print((dict1))

#update the given dictionary
dict1.update({"qualification":"btech","role":"training"})
print(dict1)
print(dict1.keys())
print(dict1.values())

#add keys and values
dict_keys = (['name', 'age', 'place', 'course', 'qualification', 'role'])
dict_values = (['aju', 1, 'abc', 'python', 'btech', 'training'])
print(dict(zip(dict_keys,dict_values)))


#remove one element
dict1 ={"name":"athu","age":1,"place":'abc',"course":"python"}
#dict1.pop("name")
#print(dict1)
dict1.popitem()
print(dict1)


#fromkeys
x = ("key1","key2","key3")
y =0,1,2
thisdict = dict.fromkeys(x,y)
print(thisdict)

#setdefault(update)
car ={"brand":"ford","model":"mustang","year":1964}
x = car.setdefault("color","white")
print(car)


