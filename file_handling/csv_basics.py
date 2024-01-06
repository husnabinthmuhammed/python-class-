import csv
#with open('names.csv', 'w', newline='') as csvfile:
#    fieldnames = ['first_name', 'last_name']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#    writer.writeheader()
#    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


#with open('sample.csv','r')as csvfile:
#    x = csv.reader(csvfile,delimiter ='\t')
#    for row in x:
#        print(row)
#csvfile.close()




with open('test_data.csv','w')as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["first_name","Lastname","Age","Year"])
    writer.writerow(["Nithin","PM",23,123])
    writer.writerow(["Abin","john",30,6875])




#with open('test_data.csv','w')as csvfile:
#    writer.writeheader()
#    fieldnames = ["first_name","Lastname","Age","Year"]
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    writer.writerow({"First_name":"Nithin","Lastname":"PM","Age":23,"Year":1234})
#    writer.writerow({"First_name":"Abin","Lastname":"john","Age":30,"Year":6875})
#    csvfile.close()


with open('test_data.csv','r')as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)
with open('sample_data.csv','w')as file:
    writer = csv.writer(file)
    writer.writerow(["s.no","name","course","place"])
    writer.writerow(['1','priya','python','asdfg'])
    file.close()





#import csv
#reader = csv.reader(open(r"sample.csv"),delimiter=' ')
#filtered = filter(lambda p: 'Central' == p[2], reader)
#csv.writer(open(r"sample.csv",'w'),delimiter=' ').writerows(filtered)