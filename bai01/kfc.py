#!/usr/bin/python3

from decimal import *
# with open("inp.txt", "r") as f:
# 	a, b = f.read().split()

f = input()

f = float(f)
# a = int(a)
# b = int(b)



c = (f - 32)/1.8
k = c + 273.15

getcontext().prec = 6
print(Decimal(c).normalize(), Decimal(k).normalize())