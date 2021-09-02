#!/usr/bin/python3

# with open("inp.txt", "r") as f:
# 	a, b = f.read().split()

a, b = input().split()

a = int(a)
b = int(b)
max = ((a + b) + abs(a - b)) // 2
min = ((a + b) - abs(a - b)) // 2

print(f"max = {max}")
print(f"min = {min}")