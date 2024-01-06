"""
     python programmming files
     it can be import a module by  module in the program

    1. custom module
    2. builtin module(os,random,sys..)
    3. external module(pip install)
"""
import os
import random
import time

#os.mkdir(r'C:\Users\hp\PycharmProjects\python_class\module\div')

#os.rmdir(r'C:\Users\hp\PycharmProjects\python_class\module\div')
#print(os.getcwd())
#cd.chdir('D:/')
#print(os.getcwd())

#os.chdir('')

print(random.randrange(10))

print(random.randint(1,20))
print(random.choice('computer'))
#print(random.shuffle(1,2,3,4,5))

"""
_____________QUESTION--------------------
difference b/w module and package
difference b/w package and library
difference b/w library and frame works
"""

import datetime

today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)
current_time=now.ctime()
print(current_time)
current_time=time.ctime()
print(current_time)

