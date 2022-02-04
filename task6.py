from itertools import count
from itertools import cycle


for el in count(2):
    if el > 10:
        break
    else:
        print(el)

tip = 0
for el in cycle("123"):
    if tip > 10:
        break
    print(el)
    tip += 1
    
