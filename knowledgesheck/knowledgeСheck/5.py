import re
import json
from collections import defaultdict

with open("lorem.txt", "r") as f:
    words = ''
    for line in f:
         words += line



word_list = words.split()

word_count_dict = defaultdict(int)

dicts = {}
for word in word_list:
    dicts.update({word : word_count_dict[word]})
    word_count_dict[word] += 1
print(word_count_dict)