""""

with open('maybatch.txt','r')as file:
    x=file.readlines()
    print((x))
    print((x[0]))
    x.remove('it very attractive for Rapid Application Development, as well as for use as a scripting or glue') as file:
    print(x)
    x.pop()
    print(X)for i in x:
        print(i)




#_____________delete purticular line from a file_______________

import fileinput
file ='maybatch.txt'
lines_to_delete = [3,5]

def delete_line(file,lines_to_delete):
    with fileinput.input(file,inplace=True)as file:
        for i in file:
            if file.lineno()not in lines_to_delete:
                print(i.rstrip())
delete_line(file,lines_to_delete)



#_______________python list files in a directory_____________________


import os
directory_path =r'C:\Users\hp\PycharmProjects\python class\file_handling\revision'
def list_files(directory_path):
    file = os.listdir(directory_path)
    return file
file_list = list_files(directory_path)
print(file_list)
for i in file_list:
    print(i)



#____________________count of the directory files___________________
import os
directory = r'C:\Users\hp\PycharmProjects\python class\file_handling'
def count_files(directory):
    count = 0
    list_file = os.listdir(directory)
    for i in list_file:
        count=count+1
    print(count,"num of files in the directory")
count_files(directory)




#_________________pyhton list files in directory with extension txt___________________________

def list_txt_files(directory):
    txt_files = [file for file in os.listdir(directory)if file.endwith("txt")]
    return txt_files
print(list_txt_files(directory))






""""

listitems = ['Hi','How are you','Welcome to python class']
with open("listitems.txt",w)as file:
    for i in listitems:
        file.write(i+"\n")
        #file.close()
