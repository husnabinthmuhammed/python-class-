import os
file = r'my file'
#x= os.path.exists(file)
#if x:
#    print(f'{file} the file is exists ')
#else:
#    print(f'{file}  not exists')




#file_name= "myfile"
#file=open('myfile','a')
#file.write('hi dears')
#file_size=os.stat(file_name)
#print(f'file size{file_size.st_size}')

"""
file= open('new.txt','w')
file.write('hello....\n')
with open('new.txt') as file:
    print(file.read())
file= open('new.txt','a')
file.write('welcome')
with open('new.txt') as file:
    print(file.read())
file=open('new.txt','r')
print((len(file.newlines)))
"""

"""
st=input("enter the string to be search:")
with open('new.txt') as file:
    x=file.read()
    if st in x:
         print("string is found")
    else:
        print("string is not found")
"""

"""
import linecache
specific_line=linecache.getline("new.txt",2)
print(specific_line)
"""
"""
with open('new.txt','r+') as file:
    #file.read()
    file.write('new line \n')
    file.write('second line\n')
    lines=file.read()
    print(lines)
    #file.close()
"""


#with open('new.txt','a+') as file:
#    file.seek(0)
#    lines=file.readlines()
#    print(lines)
#    file.write("\n "+str (len(lines)))
#    print(file.read())

#________________________print last element______________________

#with open('new.txt','r')as file:
#    #file.seek(2)
#    lines = file.readlines()
#    print(lines[-1])



#_______________find the longest word from a file___________________

def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        print(words)
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('new.txt'))
