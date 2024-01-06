"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

"""
#file = open('sample','x')
#file = open('sample.txt','w')
#file.write('Hi dears rjhhfihkflkj')
#file.close()


#file=open('sample.txt','r')
#print(file.read())

#file=open('sample.txt','a')
#file.write('husna')
#file.close()
#____________________________or__________________________________#
#with open('sample.txt','r')as file:
#    print(file.read())
#

#with open('sample.txt','w')as file:
#    print(file.write('New line'))

#_______________________________delete_______________________________#


#import os
#os.remove('sample.txt')


import os
file_path = r'sample.txt'
x= os.path.exists(file_path)
if x:
    print(f"{file_path}The file is existing")
else:
    print(f'the file {file_path}is not existing')