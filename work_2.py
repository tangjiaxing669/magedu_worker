#!/usr/bin/env python

import sys

int_variable = 18

for _ in range(3):
    input_num = input("Please input your num: ").strip()
    if input_num.isdigit():
        input_num = int(input_num)
    else:
        print('Input Error, Please Again. ')
        continue
    if input_num == int_variable:
        print("Congratulations! you win! ")
        sys.exit()
else:
    print("Oops! you fail! ")
