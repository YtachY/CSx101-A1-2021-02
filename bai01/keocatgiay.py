#!/usr/bin/python3

# from time import time
# from math import sqrt

# with open("inp.txt", "r") as f:
# 	a, b = list(i for i in f.read().split())

a, b = input().split()
# print(a,b,c, type(a), type(int(a)))

a = int(a)
b = int(b)
# st = time()
# -----
s1 = a * (a - 1) // 2
cuoi = b - 2
dau = b - a
s2 = (dau + cuoi) * (a - 1) // 2
result = s1 + s2
# -----
print(result)
# print(time() - st)