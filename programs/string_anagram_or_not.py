"""
write a code to check if two srings are  anagram or not
"""
str1 = input("Enter the string1:")
str2 = input("Enter the string2:")

str3= str1.lower()
str4= str2.lower()

if (len(str3)==len(str4)):
    sorted_str1= sorted (str3)
    print(sorted_str1)
    sorted_str2 = sorted(str4)
    print(sorted_str2)
    if(sorted_str1==sorted_str2):
        print(str1+" and "+str2+" are anagram.")
    else:
        print("not anagram")



