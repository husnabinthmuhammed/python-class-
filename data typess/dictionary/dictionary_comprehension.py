"""
dictionary = {key:value for vars in iterable}
"""
square_dict = dict()
for num in range(1,11):
    square_dict[num]=num*num
print(square_dict)


#_________________dictionary comprehension_______________

square_dict={num:num*num for num in range(1,11)}
print(square_dict)


#_______________________________________________________

old_price= {'milk':1.02,'coffee':2.5,"bread":2.5}
doller_to_pound = 0.76
new_price = {key: value * doller_to_pound for (key,value) in old_price.items()}
print(new_price)


#________________________________________________________


first_dict ={'jack':38,'jin':48,'juido':57,'john':89}
even_dict ={k:v for (k,v) in first_dict.items()if v%2==0}
print(even_dict)

#________________________________________________________

keys =['a','b','c','d','e']
values = [1,2,3,4,5]
dictionary = {k:v for (k,v) in zip(keys,values)}
print(dictionary)

#__________________________________________________________
original_dict = {'jack':38,'michael':48,'guido':57,'john':33}
new_dict_1={k: ('old' if v>40 else 'young')for (k,v)in original_dict.items()}
print(new_dict_1)

#______________________________________________________________

new_dict = {k:('even'if k%2==0 else 'odd')for(k)in range(1,11)}
print(new_dict)
#________________________________________________________________

keys =['a','b','c','d','e','f']
first_value = [keys[i]for i in range (0,len(keys),2)]
second_value = [keys[j]for j in range (1,len(keys),2)]
print(dict(zip(first_value,second_value)))

new_dict3 = {keys[i]:values[i+1] for i in range (0,len(keys),2)}
print(new_dict3)
