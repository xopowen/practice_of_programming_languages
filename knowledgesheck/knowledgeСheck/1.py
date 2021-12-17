import re

i = input('введите выражение')
if re.search(r'[\++\-+\*+\/+]',i) !=None:
    try:
        print(eval(i))
    except ZeroDivisionError:
        print("делить на ноль плохо")
else:
    print('тут просто строка а не математическое вырожение')

