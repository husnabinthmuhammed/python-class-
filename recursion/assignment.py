"""
1.string pallindrome
2.sum of digits
3.write a recursive fn calculate the result of  raising a number to a given power
  eg:2,3=8 2^3=8
"""
#_________________________string pallindrome_______________________________
"""
s = input("enter the string:")
def is_palindrome(s):
    if len(s) <=1:
        return True
    else:
        if s[0] == s[-1]:
            return  is_palindrome(s[1:-1])
        else:
            return False
print(is_palindrome(s))
"""





#______________________sum of digits_____________________
"""
n=234
def sum_of_digits(n):
    if n < =0 :
        return  n
    else:
        return n%10 + sum_of_digits(n//10)
print(sum_of_digits(n))

"""
#__________________

n=234
def product_of_digits(n):
    if n <  10 :
        return  n
    else:
        return n%10 * product_of_digits(n//10)
print(product_of_digits(n))


