"""____________________________JSON TO PYTHON______________________________________________"""
import json

#some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(type(y))

"""____________________________PYTHON TO JSON_____________________________________"""


import json

# a Python object (dict):
x = {"name": "John","age": 30,"city": "New York"}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))

"""__________________________ACCESS THE VALUE OF KEY 2 FROM THE FOLLOWING JSON______________"""


import json

#some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y=json.loads(x)
print(y["age"])


"""-------------ACCESS THE NESTED KEY "salary" from the following json----------------

import json
samplejson= '{"company":{"employee":{"name":"emma","payble":{"salary":7000,"bonus":800}}}}'
y = json.loads(x)
print(y["company"]["employee"]["payble"]["salary"])"""


"""_________________generate alphabetic hex colors randomly_________________________________"""
import random
color = "%06x" %random.randint(0,0xFFFFF)
print(color)


"""________________________random multiple of 7_____________"""
import random
print("generete random multiple of 7 b/w 0 and 70:")
print(random.randint(0,10)*7)

"""________________________"""