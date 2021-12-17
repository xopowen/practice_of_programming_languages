import random

arr = [random.triangular(-100.0, 101.0, 0.1) for i in range(10)]
arr = sorted(arr, key = lambda x: abs(x - int(x)) , reverse = True)
print(arr)
