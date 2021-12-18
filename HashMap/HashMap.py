import re

class SpecialHashMap(dict):

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):

        if key is not  self.__dict__.keys():
            raise KeyError ("такого ключя нет")
        return self.__dict__[key]


    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):

        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __clearingItems(self,sort_len_list):

        for i in range(len(sort_len_list)):
            if sort_len_list[i].count(",") > 0:
                if sort_len_list[i][0].isdigit() == False:
                    sort_len_list[i] = sort_len_list[i][1:-1]
                    sort_len_list[i] = tuple(map(int, sort_len_list[i].split(',')))
                else:
                    sort_len_list[i] = tuple(map(int, sort_len_list[i].split(',')))
            else:

                if sort_len_list[i][0].isdigit():

                    sort_len_list[i] = tuple(map(int, sort_len_list[i]))

        return sort_len_list


    @property
    def iloc(self,yallue = None):
        sort_dict = sorted(list(self.__dict__.items()))
        res_dict = [ i[1] for i in sort_dict]
        if yallue is None:
            return res_dict
        return self.__dict__

    def __ploc_dop(self,list_make):

        sort_len_list_str = list(filter(lambda x: len( x.split(",") ) == len(list_make), self.__dict__.keys()))
        sort_tuple = self.__clearingItems( sort_len_list_str.copy() )
        kit_sets =[]

        operator, nemper ='',''
        for i in range(len(list_make)):
            if len(list_make[i]) == 2:
                operator,nemper = list_make[i][0][-1], int(list_make[i][1])

                kit_sets.append( self.predSobajie(operator, nemper, -1, sort_tuple))
            else:
                operator, nemper = list_make[i][0:2], int(list_make[i][-1])

                kit_sets.append(self.predSobajie(operator, nemper,-1, sort_tuple))
        kit_sets = list(kit_sets[0].intersection(*kit_sets))
        result = {}

        for i in range(len(kit_sets)):
            key = sort_tuple.index(kit_sets[i])
            result.update({str(kit_sets[i]):self.__dict__[str(sort_len_list_str[key])]})



        return result

    def predSobajie(self,operator,nemper,position,sort_len_list):

        if operator == ">=":
            return set(filter(lambda x:int(x[position]) >= nemper, sort_len_list))
        elif operator == ">":
            return set(filter(lambda x: int(x[position]) > nemper , sort_len_list))

        elif operator == "<":
            return set(filter(lambda x: int(x[position]) < nemper, sort_len_list))

        elif operator == "<=":
            return set(filter(lambda x: int(x[position]) <= nemper, sort_len_list))

        elif operator == "==":
            return set(filter(lambda x: int(x[position]) == nemper, sort_len_list))

        elif operator == "<>":
            return set(filter(lambda x: int(x[position]) != nemper, sort_len_list))
        else:
            raise ValueError('условие неверное')

    def ploc(self,*args):
        sting = str(*args)
        list_conditions = []
        item_condition = ''
        if sting == '':
            raise ValueError('условие неверное')
        #находим все условия несмотря на разделители.
        for i in range(len(sting)):
            if sting[len(sting)-1].isdigit() == False:
                raise ValueError('условие неверное')
            if re.match("[>|<|=]?",sting[i]).span() != (0,0):
                if len(item_condition) == 2:

                    raise ValueError('условие неверное')
                item_condition += sting[i]
                continue
            if sting[i].isdigit():
                item_condition += sting[i]
                #"выбрасываем исключение если у  числа нет условия"
                if len(item_condition) > 0:
                    if item_condition[0].isdigit():
                        raise ValueError('условие неверное')
                list_conditions.append(item_condition)
                item_condition = ''

        return self.__ploc_dop(list_conditions)

ftf = SpecialHashMap()
ftf["value1"] = 1
ftf["value2"] = 2
ftf["value3"] = 3
ftf["1"] = 10
ftf["2"] = 20
ftf["3"] = 30
ftf["1, 5"] = 100
ftf["5, 5"] = 200
ftf["10, 5"] = 300
ftf["1, 5, 3"] = 400
ftf["5, 5, 4"] = 500
ftf["10, 5, 5"] = 600

print(ftf.ploc(">=1,>1"))
