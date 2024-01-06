"""
_______________________________________________________________
wap to remove all the repeating letters from each words of a given sentence.
Eg:
          i/p:Let's google the pineapple
          o/p:Let's gole the pineal
________________________________________________________________


str1 = "Let's google the pineapple"
str2 = str1.split(' ')#[
#print(str2)
str3 = []
for i in str2:
    #print(i)
    k = ""
    for j in i:
        #print(j)
        if j in k:
            continue
        else:
            k=k+j
    print(k)
    str3.append(k)
    print(str3)
print(" ".join(str3))

"""
"""
______________________________________________________________________
given a sentence,reverse each word but don't reverse the sentence
_____________________________________________________________________

str = "Let's google the pineapple"
str1 = str.split(' ')
#print(str2)
re_word = []
for word in str1:
    word = word[::-1]
    re_word.append(word)
print(re_word)
print(" ".join(re_word))

"""

str = '2345678765432'
num = []
even =[]
odd = []
for i in str:
    num.append(int(i))
for j in num:
    if j%2 ==0:
        even.append(j)
    else:
        odd.append(j)
print(odd)
odd.sort()
even.sort(reverse=True)
print(odd)
even_int = [str[x]for x in even]
odd_int = [str[y]for y in odd]
print((even_int))
print((odd_int))
#lastnum = print(''.join(lastnum\odd_int+even_int)