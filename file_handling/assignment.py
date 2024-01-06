"""
1.	Write a Python program to read first n lines of a file.
2.	Write a Python program to read last n lines of a file.
3.	Write a Python program to count the frequency of words in a file.
4.	Write a Python program to copy the contents of a file to another file
5.	Write a Python program to read a random line from a file.
6.	Write a Python program that takes a text file as input and returns the number of words of a given text file.
"""
#___________________1.	Write a Python program to read first n lines of a file.________________________


def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head('new.txt', 2)


#_____________________2.	Write a Python program to read last n lines of a file._____________________________

import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break

file_read_from_tail('new.txt',2)



#___________________3.	Write a Python program to count the frequency of words in a file______________


from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("new.txt"))



#__________________4.	Write a Python program to copy the contents of a file to another file___________________

from shutil import copyfile
copyfile('new.txt', 'abc.txt')


#____________________5.	Write a Python program to read a random line from a file._____________________________

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('new.txt'))


#________________6.	Write a Python program that takes a text file as input and returns the number of words of a given text file.

def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("new.txt"))