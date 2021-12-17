import re

lett = "AIEOUY"
word = input()
n = sum((1 for i in word.upper() if i in lett))
if n != None:
    print(n)
else:
    print("0")