#!/usr/bin/python3

# with open("inp.txt", "r") as f:
# 	a, b = f.read().split()

a, b = input().split()

a = int(a)
b = int(b)

x = 2 * a - b // 2
y = a - x

print(x, y)