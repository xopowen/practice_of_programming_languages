word_one = set('test')
word_two = set('exam')
#пересечение множеств
с = word_one & word_two

t = len(с) / (len(word_one) + len(word_one))
print(t)