import re

lett = "AIEOUY"
lett2 = "QWRTYPSDFGHJKLZXCVNM"
word = input('тут нужно что то...слово, фраза, мат:')
n = sum((1 for i in word.upper() if i in lett))
m = sum((1 for i in word.upper() if i in lett2))
if n != None:
    print("гласных: " + str(n),"согласные: " + str(m))
else:
    print("0")