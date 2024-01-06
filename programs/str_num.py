"""
str = "123" to 123 with out using built in fn
"""

str1 = "123"
result = 0
for i in str1:
    digits = ord(i) - ord ('0')
    print(digits)
    result= result*10+digits
    print(result)
    print(type(result))