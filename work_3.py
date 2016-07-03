#!/usr/bin/env python

rep_list = [1, 3, 2, 4, 3, 2, 5, 5, 7]

list_temp = []

for i in rep_list:
    if i not in list_temp:
        list_temp.append(i)
print(list_temp)
