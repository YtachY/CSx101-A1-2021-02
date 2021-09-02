#!/usr/bin/python3

from time import time
from math import sqrt

# with open("inp.txt", "r") as f:
# 	a, b, c = list(i for i in f.read().split())


# def sqrt(n):
#     # 3 iterations of newton's method, hard-coded
#     # normalize

#     # find highest bit
#     highest = 1
#     sqrt_highest = 1
#     while highest < n:
#         highest <<= 2
#         sqrt_highest <<= 1

#     n /= highest+0.0

#     result = (n/4) + 1
#     result = (result/2) + (n/(result*2))
#     result = (result/2) + (n/(result*2))

#     return result*sqrt_highest

a, b, c = input().split()
# print(a,b,c, type(a), type(int(a)))

a = float(a)
b = float(b)
c = float(c)
st = time()
x = pow(a, 5) - 2 * sqrt(abs(b)) + a * b * c
print("{:.2f}".format(x))

# print(time() - st)