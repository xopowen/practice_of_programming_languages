import re
import sys
import numpy as np



#проверка на чесло
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#проверка что в присланом списке 1 элемент это оператор
def faintListTree(keys) -> bool:
    #print(keys)
    try:
        if re.search(r'^[\++\-+\*+\/+]', keys[0]):
            return True
        else:
            return False
    except IndexError:
        #print(keys)
        return False


#клас лист дерево
class ListTree:
    def __init__(self, data):
        self.operator = data[0]
        self.nemper1 = data[1]
        self.nemper2 = '' if len(data) == 2 else data[-1]

    def isdigit()->bool:
        return False
    def __str__(self):
        if self.nemper2 != '':
            return "({n1}{op}{n2})".format(n1 = self.nemper1,op = self.operator,n2 = self.nemper2)
        else:
            return "({op}{n1})".format(n1 = self.nemper1,op = self.operator)

def out_of_prefix_in_infics(arr):
    checkPrefix(arr)
    while(len(arr) != 1):
        for i in range(0, len(arr)):
             stop = len(arr) - i
             start = len(arr) - 3 - i if len(arr) > 2 else - 2
             if faintListTree(arr[ start : stop ]):
                 arr = arr[:start] + [str(ListTree(arr[start : stop]))] + arr[stop:]
                 break
    return arr[0]
#проверка входных данных
def checkPrefix(arr):
    if re.search(r'[\++\-+\*+\/+]', arr[0]) :
       pass
    else:
        print('ошибка ввода')
        sys.exit()

    for i in arr:
        if re.search(r'[\++\-+\*+\/+]|[0-9]', i):
            pass
        else:
            print('ошибка ввода')
            sys.exit()
    return True

arr = input().split(' ')


print(out_of_prefix_in_infics(arr))
