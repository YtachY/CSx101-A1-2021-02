#!/usr/bin/python3

a, b = map(int, list(input().split()))

# print(a, b)

print(pow(a, b, pow(10, 9) + 7))