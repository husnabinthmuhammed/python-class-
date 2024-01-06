def search (list1, key) :

    for i in range (len (list1)):

        if key == list1 [i]:
            print("key element is found at index:",i)
            break
        else:
            print("element is not found")

list1 =[1,3,5,4,7,9,]
print(list1)
key = int(input("enter the key element: "))

search (list1, key)