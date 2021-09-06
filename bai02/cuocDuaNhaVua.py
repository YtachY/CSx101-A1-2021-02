#!/usr/bin/env python3

n = int(input())
a, b = [int(i) for i in input().split()]

distWhite = max(a, b) - 1
# print(distWhite)
distBlack = max(n - b + 1, n - a + 1) - 1
# print(distBlack)

if (distBlack < distWhite):
	print("Black")
else:
	print("White")