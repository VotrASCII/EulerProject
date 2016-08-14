from math import *
from array import *
a=pow(sum(range(1, 101)), 2)
b=0
for i in range(1, 101):
    b+=pow(i, 2)

res=a-b
print(res)
