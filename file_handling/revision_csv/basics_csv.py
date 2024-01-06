import csv
with open ('sample.csv','r')as file:
   x = csv.reader(file)
   for i in x:
       print(i)



with open('test.csv','w')as file:
    writer = csv.writer(file)
    writer.writerow(["Hi"])
    writer.writerow(["How are you"])
    writer.writerow(["Python class"])

with open('test.csv','r',newline='\n')as file:
    reader = csv.reader(file)
    print(i)



