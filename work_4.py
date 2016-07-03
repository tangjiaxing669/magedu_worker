#!/usr/bin/env python
from math import sqrt

prime = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
flag = 0

for i in prime:
    if i == 2 or i == 3: 
        print(i)
        flag +=1 
        continue
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            break
        elif i % j != 0 and j == int(sqrt(i)):
            flag += 1
            print(i)

print('flag => {0}'.format(flag))
