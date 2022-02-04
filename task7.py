from itertools import count
from math import factorial
def my_func():
    for el in count(1):
        yield factorial(el)
loss = my_func()
n = 0
for el in loss:
    if n < 6:
        print(el)
        n += 1
    else:
        break
        
