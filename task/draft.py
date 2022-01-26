import os
import sys
from string import ascii_uppercase
from collections import OrderedDict

"""dir = os.walk("/home/alexander/PycharmProjects/Duplicate File Handler/Duplicate File Handler")
for folder in dir:
    if len(folder[2]) != 0:
        for file in folder[2]:
            full_path = folder[0] + f'{os.sep}' + file
            print(full_path)"""

print(os.path.getsize("/home/alexander/PycharmProjects/Duplicate File Handler/Duplicate File Handler/task/handler.py"))


print((7 % 13) % 5)

a = 3
m = 13

od = OrderedDict(enumerate(ascii_uppercase))
print(od)

"MBCD"
"QBAE"
"BBACD"
print((13*(3**0) + 2*(3**1) + 3*(3**2) + 4*(3**3)) % 13)
print((17*(3**0) + 2*(3**1) + 1*(3**2) + 5*(3**3)) % 13)
print((2*(3**0) + 2*(3**1) + 1*(3**2) + 3*(3**3) + 4*(3**4)) % 13)



d = {1: 'a', 2: 'b', 4: 'c'}
d_ = {1: 'a', 2: 'b', 4: 'c', 5: 'e'}
print(set(d).issubset(set(d_)))

numbers = [int(x) for x in input().split()]
print(numbers)
