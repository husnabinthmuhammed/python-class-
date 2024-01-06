import re

text = "ABCABCDAB"
substring =  "AB"
matches = re.findall(substring, text)
count = len(matches)
print(f"The substring '{substring}' appears {count} times in the text.")









